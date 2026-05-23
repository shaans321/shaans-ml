"""
Talking to Models - Messages System
Models understand structured conversations through messages:
 System (instructions), Human (user), and AI (assistant) messages.


**** Message Flow:
SYSTEM: You are a helpful assistant
HUMAN: What's your name?
AI: I'm your AI assistant!

"""
import os
import certifi
from dotenv import load_dotenv
from pathlib import Path
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# Load .env from the repository root

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

# Ensure certificate validation works on Windows
os.environ.setdefault("SSL_CERT_FILE", certifi.where())

# Initialize model with base_url
model = ChatOpenAI(
    #model="openai/gpt-4.1-mini",
    model="llama-3.3-70b-versatile",  # Fast, free model
    temperature=0,
    base_url=os.environ.get("GROQ_API_BASE"),
    api_key=GROQ_API_KEY,
)

# Structure your conversation
messages = [
    SystemMessage(content="You are a helpful Python tutor"),
    HumanMessage(content="Explain variables to a beginner")
]

# Send to model
response = model.invoke(messages)
print("User: Explain variables to a beginner")
print(f"AI: {response.content}")

# Build a conversation with history
print("\n=== Conversation with Memory ===")
chat_history = [
    SystemMessage(content="You are a friendly assistant who remembers everything"),
    HumanMessage(content="My name is Alice and I love pizza")
]

# Get first response
ai_response = model.invoke(chat_history)
print("First response:", ai_response.content)

# Add AI response to history
chat_history.append(ai_response)

# Continue conversation
chat_history.append(HumanMessage(content="What's my name and what do I like?"))
response = model.invoke(chat_history)
print("\nAssistant remembers:", response.content)

messages_complete_path = script_dir / "messages-complete.txt"
messages_complete_path.write_text("MESSAGES_COMPLETE")