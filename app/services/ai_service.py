# Ai logic for the application

import os
import requests
from dotenv import load_dotenv
from fastapi import HTTPException


load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"
}

def get_stock_analysis(stock: str):

    return f"""
    {stock} shows moderate growth potential

    Trend:
    Stable upward movement

    Risks:
    Market volatility and sector pressure

    Outlook:
    Positive long-term outlook.
    """
    
    try:
        response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt},
        timeout=30,
        proxies={
            "http": None,
            "https": None
        }
    )

        print("REQUEST URL:", response.url)
        print("STATUS:", response.status_code)
        print("RAW TEXT:", response.text)

        if response.status_code != 200:
            return f"HuggingFace API error: {response.status_code} | {response.text}"
        
        result = response.json()
        print("PARSED RESULT:", result)

        if isinstance(result, list) and len(result) > 0:
            generated_text = result[0].get("generated_text")

            if generated_text:
                return generated_text
            return "No generated text found in the response"
        
        return "Invalid response format from HuggingFace"
    
    except requests.exceptions.RequestException as e:
        return f"Request Error: {str(e)}"
    except Exception as e:
        return f"Unexpected Error: {str(e)}"