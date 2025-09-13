# 📄 Document Summarizer  

An AI-powered **Document Summarizer** built with **Google Gemini AI** and **Streamlit**.  
This tool helps you quickly extract key insights from large documents by splitting text into chunks, generating summaries, and combining them into a final concise overview.  

---

## 🚀 Features  
- Summarize long documents into short bullet points  
- Handles large text by splitting into smaller chunks  
- Retry mechanism for Gemini API when servers are overloaded  
- Clean and scalable code structure (`summarizer/` package)  
- `.env` support for safe API key management  

---

## 🛠️ Tech Stack  
- **Python 3.11+**  
- **Google Gemini AI API (`google-genai`)**  
- **Streamlit** for the UI  
- **LangChain** (for text splitting)  
- **dotenv** for environment variable management  

---

## 📂 Project Structure  
Document-Summarizer/
│── app.py                 # Streamlit app entry point

│── .env                   # Your API key (ignored in git)

│── .env.example           # Example env file (safe to push)

│── requirements.txt        # Dependencies

│── summarizer/

│   ├── __init__.py        # Package init

│   ├── summarize.py       # Summarization logic

│   └── utils.py           # (Optional) helper functions
