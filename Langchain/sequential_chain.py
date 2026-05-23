import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
from pathlib import Path

# Load .env
script_dir = Path(__file__).resolve().parent
load_dotenv(script_dir / ".env")

# Get Groq API key (sign up at console.groq.com)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Add this to your .env
GROQ_API_BASE = os.getenv("GROQ_API_BASE")  # Optional: set custom base URL

# Initialize model with proxy
model = ChatOpenAI(
    #model="openai/gpt-4.1-mini",
    model="llama-3.3-70b-versatile",  # Fast, free model
    temperature=0,
    #base_url=os.environ.get("OPENAI_API_BASE")
    base_url=GROQ_API_BASE,
    api_key=GROQ_API_KEY
)

# Create a prompt template
prompt = ChatPromptTemplate.from_template(
    "You are a helpful assistant. Answer this question: {question}"
)

# Create output parser
parser = StrOutputParser()

# Build the chain using LCEL pipe operator
chain = prompt | model | parser

# Execute the chain
result = chain.invoke({"question": "What is LCEL in LangChain?"})

print("User: What is LCEL in LangChain?")
print(f"AI: {result}")

# Chain with multiple steps
print("\n=== Multi-Step Chain ===")

# Step 1: Generate a topic
topic_prompt = ChatPromptTemplate.from_template(
    "Generate a creative topic about {subject}"
)

# Step 2: Write a story about that topic  
story_prompt = ChatPromptTemplate.from_template(
    "Write a 2-sentence story about: {topic}"
)

# Build a multi-step chain
multi_chain = (
    {"topic": topic_prompt | model | parser}
    | story_prompt
    | model
    | parser
)

story = multi_chain.invoke({"subject": "robots"})
print(f"Generated Story: {story}")

# Using RunnablePassthrough to preserve input
print("\n=== Chain with Passthrough ===")

from langchain_core.runnables import RunnableParallel

chain_with_context = RunnableParallel(
    {
        "original": RunnablePassthrough(),
        "response": prompt | model | parser
    }
)

result_with_context = chain_with_context.invoke({"question": "What is 2+2?"})
print(f"Original Input: {result_with_context['original']}")
print(f"Response: {result_with_context['response']}")

with open(script_dir / "sequential-chains.txt", 'w') as f:
    f.write("SEQUENTIAL_CHAINS_COMPLETE")