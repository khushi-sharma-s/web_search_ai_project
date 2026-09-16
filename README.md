# 🌐 Web Search AI Agent (Gemini 3.6 Flash)

An advanced, real-time AI Assistant built using the modern **LangChain Framework** and **Google Gemini (gemini-3.6-flash)**. This agent dynamically searches the web using DuckDuckGo to provide accurate, up-to-date answers to your queries.

The project features both a **Command-Line Interface (CLI)** version and a beautiful **Streamlit Web UI**.

---

## ✨ Features

- **🧠 Modern Agentic Workflow:** Built using LangChain's latest `create_agent` ecosystem with native tool-calling capabilities.
- **⚡ Real-Time Web Search:** Integrates DuckDuckGo Search (DDGS) to bypass LLM knowledge cutoffs and fetch live information.
- **🚀 Optimized Performance:** Implements Streamlit's `@st.cache_resource` to cache the agent instance, preventing redundant model re-initialization on user interaction.
- **🔒 Production-Ready Security:** Fully decoupled API key management using `python-dotenv` and secure `.gitignore` patterns.

---

## 📁 Project Structure

```text
├── app.py                # Streamlit Web UI Code
├── main.py               # Normal CLI / Terminal Code
├── .gitignore            # Protects secret keys (ignores .env)
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation (This file)
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com
cd YOUR_REPOSITORY_NAME
```

### 2. Install Dependencies
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables
Create a file named `.env` in the root directory and add your Google Gemini API key:
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

---

## 💻 How to Run

### Option A: Run the CLI Version (Terminal)
To quickly ask a question inside your terminal:
```bash
python main.py
```

### Option B: Run the Streamlit Web Application
To launch the beautiful conversational chat interface in your browser:
```bash
streamlit run app.py
```

---

## 🛠️ Tech Stack & Architecture

- **Core Brain:** Google Gemini (`gemini-3.6-flash`)
- **Orchestration:** LangChain Core & Agent Architecture
- **Web UI:** Streamlit (Chat Interface components)
- **Search Tool:** DuckDuckGo Search API (`duckduckgo-search`)
