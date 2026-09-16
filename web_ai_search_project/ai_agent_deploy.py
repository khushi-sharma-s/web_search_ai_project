import os
import streamlit as st
from dotenv import load_dotenv
# Modern LangChain Framework & Gemini Imports
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from duckduckgo_search import DDGS

# Load environment variables (reads GEMINI_API_KEY from .env file)
load_dotenv()

# Streamlit Page Configuration
st.set_page_config(page_title="Web Search AI", page_icon="🌐", layout="centered")
st.title("🌐 Web Search AI")
st.caption("A simple AI assistant that searches the web to answer your questions in real time.")

# --- 1. AGENT INITIALIZATION (WITH CACHING) ---
@st.cache_resource
def initialize_agent():
    """Cache the agent to prevent reloading the model on every user interaction"""
    @tool
    def duckduckgo_search(query: str) -> str:
        """Use this tool to search the internet for current information and facts."""
        try:
            with DDGS() as ddgs:
                results = [r['body'] for r in ddgs.text(query, max_results=3)]
            return "\n".join(results) if results else "No results found."
        except Exception as e:
            return f"Error during search: {str(e)}"

    # Google Gemini Model and Tools setup
    model = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0.7)
    tools = [duckduckgo_search]

    # Modern Agent Setup
    return create_agent(model=model, tools=tools)

# Activate the agent
agent = initialize_agent()

# --- 2. CHAT HISTORY MANAGEMENT ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! How can I help you today?"}
    ]

# Render chat history on the screen
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# --- 3. LIVE USER INPUT HANDLING ---
if user_input := st.chat_input("Ask me anything..."):
    # Display user input instantly
    with st.chat_message("user"):
        st.write(user_input)

    # Agent dynamic processing block
    with st.chat_message("assistant"):
        with st.spinner("Searching the web..."):
            try:
                # Pass dynamic user input directly into agent.invoke
                response = agent.invoke({
                    "messages": [{"role": "user", "content": user_input}]
                })
                
                # Extract the agent's output
                final_answer = response["messages"][-1].content
                st.write(final_answer)
                
                # Append to history to maintain conversational context
                st.session_state.messages.append({"role": "user", "content": user_input})
                st.session_state.messages.append({"role": "assistant", "content": final_answer})
                
            except Exception as e:
                st.error(f"Execution Error: {str(e)}")
