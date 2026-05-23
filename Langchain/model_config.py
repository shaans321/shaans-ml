"""
Control your model's behavior with temperature: 0 = precise & consistent, 1 = creative & varied.

Temperature scale : 0.0 - Precise, deterministic responses (good for factual queries)
0.5 - Balanced responses with some creativity (good for general use)
1.0 - Highly creative and varied responses (good for brainstorming, storytelling)

"""
import os
from langchain_openai import ChatOpenAI
from openai import base_url
from pathlib import Path
import os
from dotenv import load_dotenv

# Load .env
script_dir = Path(__file__).resolve().parent
load_dotenv(script_dir / ".env")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Add this to your .env
GROQ_API_BASE = os.getenv("GROQ_API_BASE")  # Optional: set custom base URL if needed
if not GROQ_API_KEY:
    print("❌ GROQ_API_KEY not found in .env file")
    print("Get your free key at: https://console.groq.com")
    exit(1)

# Precise model for facts (low temperature)
precise_model = ChatOpenAI(
    model="llama-3.3-70b-versatile",
    temperature=0,      # Very consistent answers
    max_tokens=150,    # Limit response length
    base_url=GROQ_API_BASE,
    api_key=GROQ_API_KEY
)

# Creative model for stories (high temperature)
creative_model = ChatOpenAI(
    model="llama-3.3-70b-versatile",
    temperature=0.9,    # Very creative
    max_tokens=200,
    base_url=GROQ_API_BASE,
    api_key=GROQ_API_KEY
)

# Test both behaviors with same prompt
prompt = "Describe a rainbow"

print("=== PRECISE MODEL (temp=0) ===")
print(precise_model.invoke(prompt).content)

print("\n=== CREATIVE MODEL (temp=0.9) ===")
print(creative_model.invoke(prompt).content)

# Streaming for real-time responses
streaming_model = ChatOpenAI(
    model="llama-3.3-70b-versatile",
    temperature=0.5,
    streaming=True,  # Enable streaming
    base_url=GROQ_API_BASE,
    api_key=GROQ_API_KEY
)

print("\n=== STREAMING RESPONSE ===")
for chunk in streaming_model.stream("Write a haiku about coding"):
    print(chunk.content, end="", flush=True)
print()  # New line after streaming

with open(script_dir / "config-complete.txt", 'w') as f:
    f.write("CONFIG_COMPLETE")