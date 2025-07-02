# Deprecated: Streamlit app is no longer used. Frontend is now handled by static HTML/CSS/JS with FastAPI backend.

import streamlit as st
import requests
import json
import pandas as pd

MISTRAL_API_KEY = ""
MISTRAL_MODEL = ""

# Function to chat with CSV using Mistral (OpenRouter)
def chat_with_csv_mistral(df, prompt):
    # Convert the dataframe to a CSV string (or sample, or summary)
    csv_sample = df.head(20).to_csv(index=False)  # Limit to 20 rows for prompt size
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
        # Extract the assistant's reply
        return result["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

st.set_page_config(layout='wide')
st.title("ChatCSV powered by Mistral LLM")

input_csv = st.file_uploader("Upload your CSV file", type=['csv'])

if input_csv is not None:
    col1, col2 = st.columns([1,1])
    with col1:
        st.info("CSV Uploaded Successfully")
        data = pd.read_csv(input_csv)
        st.dataframe(data, use_container_width=True)
    with col2:
        st.info("Chat Below")
        input_text = st.text_area("Enter your query")
        if input_text is not None:
            if st.button("Chat with CSV"):
                st.info("Your Query: "+input_text)
                result = chat_with_csv_mistral(data, input_text)
                st.success(result)

