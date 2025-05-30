# code_engine/gemini_client.py
import google.generativeai as genai
import os
from dotenv import load_dotenv
import re

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")
def generate_code(prompt):
    enhanced_prompt = (
        "Write only Python code. "
        "Do not use markdown formatting like ```python. "
        "Do not add explanations or comments. Output only the raw Python code.\n\n"
        f"{prompt}"
    )
    response = model.generate_content(enhanced_prompt)
    raw_code = response.text.strip()

    # 🔥 Strip common markdown wrappers if Gemini includes them anyway
    if raw_code.startswith("```python"):
        raw_code = raw_code[len("```python"):].strip()
    if raw_code.endswith("```"):
        raw_code = raw_code[:-3].strip()

    return raw_code
