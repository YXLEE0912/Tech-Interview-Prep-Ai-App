# Tech-Interview-Prep-Ai-App
A GenAI practice project that takes any technical concept and generates:
1. A clear, non-jargon technical explanation
2. A real-world practical example
3. Top 3 follow-up interview questions with model answers


## 🛠️ Tech Stack & Key Concepts

- *LangChain (init_chat_model, PromptTemplate)*: Dynamic prompt structuring and chat model invocation.
- *OpenAI (gpt-4o-mini)*: Fast, cost-efficient chat completions.
- *Gradio (gr.Interface)*: Rapid UI prototyping in pure Python.
- *Python-dotenv*: Secure environment variable loading for API keys.


## ⚙️ Quick Setup

1. Install Dependencies
pip install langchain langchain-core langchain-openai gradio python-dotenv

2. Set API Key
Create a .env file in the same folder:
OPENAI_API_KEY=your_openai_api_key_here

3. Run the Script
python app.py
