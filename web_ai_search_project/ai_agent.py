import os
from dotenv import load_dotenv

# 1. Naya Modern LangChain Agent Import
from langchain.agents import create_agent
import langchainhub as hub


# 2. Google Gemini Import
from langchain_google_genai import ChatGoogleGenerativeAI

# 3. Custom Tool Setup (Bina langchain-community ke)
from langchain_core.tools import tool
from duckduckgo_search import DDGS

load_dotenv()

@tool
def duckduckgo_search(query: str) -> str:
    """Use this tool to search the internet for current information and facts."""
    try:
        with DDGS() as ddgs:
            results = [r['body'] for r in ddgs.text(query, max_results=3)]
            return "\n".join(results) if results else "No results found."
    except Exception as e:
        return f"Error during search: {str(e)}"

# Model initialize (gemini-3.6-flash agentic model)
model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash", 
    temperature=0.7
)

tools = [duckduckgo_search]

#(ismein AgentExecutor ki zaroorat nahi padti)
agent = create_agent(
    model=model,
    tools=tools
)

# Invoke karein
if __name__ == "__main__":
    # Naye system mein input list/messages ke roop mein jata hai
    response = agent.invoke({
        "messages": [{"role": "user", "content": "3 ways to reach goa from delhi"}]
    })
    
    print("\n--- Final Output ---")
    print(response["messages"][-1].content)
