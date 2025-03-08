import requests
import os

OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://ollama:11434/api/generate")

def ollama_generate(prompt: str) -> str:
    payload = {"model": "mistral", "prompt": prompt}
    response = requests.post(OLLAMA_API_URL, json=payload)
    return response.json().get("response", "").strip()
