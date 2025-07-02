from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import pandas as pd
import requests
import json
from typing import Optional

app = FastAPI()

# Allow CORS for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static directory for frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

MISTRAL_API_KEY = "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"
MISTRAL_MODEL = "mistralai/mistral-small-3.2-24b-instruct:free"

# In-memory storage for the uploaded CSV (per process, not per user)
uploaded_df: Optional[pd.DataFrame] = None

@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")

@app.post("/upload")
def upload_csv(file: UploadFile = File(...)):
    global uploaded_df
    try:
        uploaded_df = pd.read_csv(file.file)
        # Return a preview (first 10 rows)
        preview = uploaded_df.head(10).to_dict(orient="records")
        columns = list(uploaded_df.columns)
        return {"success": True, "preview": preview, "columns": columns}
    except Exception as e:
        return JSONResponse(status_code=400, content={"success": False, "error": str(e)})

@app.post("/chat")
def chat_with_csv(prompt: str = Form(...)):
    global uploaded_df
    if uploaded_df is None:
        return JSONResponse(status_code=400, content={"success": False, "error": "No CSV uploaded yet."})
    # Use the same logic as in app.py
    csv_sample = uploaded_df.head(20).to_csv(index=False)
    user_message = f"Given the following CSV data:\n{csv_sample}\n\nAnswer the following question about the data:\n{prompt}"
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MISTRAL_MODEL,
        "messages": [
            {"role": "user", "content": user_message}
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        result = response.json()
        answer = result["choices"][0]["message"]["content"]
        return {"success": True, "answer": answer}
    else:
        return JSONResponse(status_code=500, content={"success": False, "error": response.text}) 