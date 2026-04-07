import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    response = openai.models.list()
    print("API key hợp lệ!")
except Exception as e:
    print("API key KHÔNG hợp lệ hoặc bị lỗi:", e)