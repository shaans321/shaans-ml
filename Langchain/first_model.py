"""
ChatOpenAI connects to OpenAI-compatible APIs. With our proxy server, you can access multiple models through one interface!
"""
import os
import certifi
from dotenv import load_dotenv
from pathlib import Path
from langchain_openai import ChatOpenAI

# Load .env from the script's directory
script_dir = Path(__file__).resolve().parent
load_dotenv(script_dir / ".env")
print("OPENAI_API_KEY loaded:", bool(os.getenv("OPENAI_API_KEY")))

# Ensure certificate validation works on Windows
os.environ.setdefault("SSL_CERT_FILE", certifi.where())

# Environment variables OPENAI_API_KEY and OPENAI_API_BASE are pre-configured

# Initialize your first model - ultra fast!
model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    base_url=os.environ.get("OPENAI_API_BASE")
)

# Test it with a simple question
response = model.invoke("Hello! What's 2+2?")
print("User: Hello! What's 2+2?")
print(f"AI: {response.content}")

# Try another question
response = model.invoke("What's the capital of France?")
print("\nUser: What's the capital of France?")
print(f"AI: {response.content}")

# Save progress
first_model_path =   "first-model.txt"
first_model_path.write_text("FIRST_MODEL_COMPLETE")