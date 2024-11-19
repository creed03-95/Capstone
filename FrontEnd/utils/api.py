import requests
import streamlit as st

class APIClient:
    def __init__(self):
        self.base_url = "http://localhost:8000/api/v1"
    
    def chat_completion(self, prompt, temperature, top_p):
        response = requests.post(
            f"{self.base_url}/chat",
            json={
                "prompt": prompt,
                "context": f"Temperature: {temperature}, Top_P: {top_p}"
            }
        )
        return response.json()