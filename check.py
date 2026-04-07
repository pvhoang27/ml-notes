import os
import requests

# Đọc API key từ biến môi trường hoặc file .env
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    # Nếu không có biến môi trường, thử đọc từ file .env
    from dotenv import load_dotenv
    load_dotenv()
    API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    print("Không tìm thấy GOOGLE_API_KEY.")
    exit(1)

# Kiểm tra key bằng cách gọi endpoint models.list của Gemini API
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

response = requests.get(url)
if response.status_code == 200:
    print("GOOGLE_API_KEY hợp lệ!")
    data = response.json()
    print("Các model bạn có thể sử dụng (có thể bao gồm model miễn phí):")
    for model in data.get("models", []):
        print(f"- {model.get('name')}")
else:
    print("GOOGLE_API_KEY không hợp lệ hoặc không có quyền truy cập.")
    print("Chi tiết lỗi:", response.text)