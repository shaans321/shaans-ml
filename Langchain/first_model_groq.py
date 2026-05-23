"""
Using Groq's Llama models with ChatOpenAI (OpenAI-compatible interface)
FREE: 14,400 requests/day, no credit card required
"""
import os
import certifi
from dotenv import load_dotenv
from pathlib import Path
from langchain_openai import ChatOpenAI

# Load .env
script_dir = Path(__file__).resolve().parent
load_dotenv(script_dir / ".env")

# Get Groq API key (sign up at console.groq.com)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Add this to your .env
GROQ_API_BASE = os.getenv("GROQ_API_BASE")  # Optional: set custom base URL if needed

if not GROQ_API_KEY:
    print("❌ GROQ_API_KEY not found in .env file")
    print("Get your free key at: https://console.groq.com")
    exit(1)

# Initialize Groq's Llama 3.3 70B (free tier)
model = ChatOpenAI(
    model="llama-3.3-70b-versatile",  # Fast, free model
    temperature=0,
    base_url=GROQ_API_BASE or "https://api.groq.com/openai/v1",
    api_key=GROQ_API_KEY,
    max_retries=2,
)

# Test it
try:
    response = model.invoke("Hello! What's 2+2?")
    print("User: Hello! What's 2+2?")
    print(f"AI: {response.content}")

    response = model.invoke("What's the capital of France?")
    print("\nUser: What's the capital of France?")
    print(f"AI: {response.content}")

    print("\n✅ Success! Groq API is working")
    
except Exception as e:
    print(f"❌ Error: {e}")