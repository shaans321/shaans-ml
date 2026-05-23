## Task 2: Master Prompt Templates - The Foundation
"""
Template Transformation Pipeline

Template "Tell me about {topic} in {language}." + Variables: topic=langchain = Result (Ready for LLM)

Basic templates are the simplest form - a string with placeholders like {variable} that get replaced with actual values.
"""

from langchain_core.prompts import PromptTemplate
from pathlib import Path

# 1. Create a basic template
template = PromptTemplate(
    input_variables=["product", "feature"],
    template="Generate a marketing slogan for {product} highlighting {feature}."
)

# 2. Use the template
prompt = template.format(product="LangChain", feature="AI orchestration")
print("Generated prompt:", prompt)

# 3. Try different variables
examples = [
    {"product": "Smartphone", "feature": "camera quality"},
    {"product": "Electric Car", "feature": "eco-friendly"},
    {"product": "AI Assistant", "feature": "natural conversation"}
]

for example in examples:
    result = template.format(**example)
    print(f"• {result}")

# Save progress
Path("venv/source/templates/basic-templates.txt").write_text("BASIC_TEMPLATES_COMPLETE")
