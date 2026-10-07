import os
from dotenv import load_dotenv
from openai import OpenAI
from config import BASE_URL,MODEL
load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")
if not api_key:
    raise ValueError("DASHSCOPE_API_KEY 未配置")
client = OpenAI(
    api_key=api_key,
    base_url=BASE_URL)

def call_llm(prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": (prompt)}])
    text=response.choices[0].message.content
    return text