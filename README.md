# 📊 ChatCSV – Chat with Your CSV Using Mistral LLM

![Screenshot 2025-07-08 204628](https://github.com/user-attachments/assets/519efc8c-e061-45c3-8425-d460a56b9bd6)


ChatCSV is a lightweight web app that lets you **interact with your CSV files using natural language**. Built with **FastAPI** and a **static HTML/CSS/JS frontend**, it uses **Mistral LLM via OpenRouter** to provide intelligent responses based on your data.

> ⚠️ Note: The previous Streamlit version (`app.py`) is deprecated. The app now runs with a FastAPI backend and static frontend.

---

## 🚀 Features

- 📁 Upload your own CSV file
- 💬 Ask questions like “What is the average salary?” or “Which product sold the most?”
- 🧠 Powered by Mistral LLM (through OpenRouter API)
- ⚡ Fast and simple – no database required
- 🌐 Accessible through a local web browser

---

## 🛠️ Tech Stack

- **FastAPI** – Backend API
- **Static HTML/CSS/JS** – Frontend UI (served from `/static`)
- **Mistral LLM via OpenRouter** – LLM inference engine
- **Pandas** – CSV processing
- **Uvicorn** – ASGI server

---

## 📂 Folder Structure

```
.
├── main.py           # FastAPI backend
├── app.py            # (Deprecated) Streamlit version
├── requirements.txt  # Python dependencies
├── .gitignore
└── static/           # Frontend files (index.html, style.css, etc.)
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/chatcsv.git
cd chatcsv
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

### 1. Start the FastAPI backend

```bash
uvicorn main:app --reload
```

### 2. Open in browser

Go to: [http://localhost:8000](http://localhost:8000)  
It will automatically redirect to `/static/index.html`.

---

## 🧪 Example Usage

1. Upload a CSV file with tabular data.
2. Enter queries like:
   - "What is the average age?"
   - "List top 5 products by revenue"
3. Get real-time answers from the LLM.

---

## 🔐 API Keys

The backend uses the OpenRouter API with a hardcoded Mistral key.

> 🚨 You should **replace the placeholder key** with your own for production use:
- Go to [https://openrouter.ai](https://openrouter.ai) and sign up for an API key.
- Replace the `MISTRAL_API_KEY` in `main.py` with your actual key.

---

## 📝 License

This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenRouter](https://openrouter.ai/)
- [Mistral](https://mistral.ai/)
- [Pandas](https://pandas.pydata.org/)
