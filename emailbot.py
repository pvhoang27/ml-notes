import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()
# 1. Cấu hình API Key (chìa khóa để gọi LLM)
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Thiếu GEMINI_API_KEY. Hãy set biến môi trường trước khi chạy.")

genai.configure(api_key=api_key)

# 2. Định hình tính cách và nhiệm vụ cho Agent (System Prompt)
he_thong_huong_dan = """
Bạn là nhân viên chăm sóc khách hàng xuất sắc của công ty điện máy ABC. 
Nhiệm vụ của bạn là đọc email phàn nàn hoặc thắc mắc của khách hàng, sau đó viết email phản hồi.
Quy tắc:
- Xưng hô: Dạ/Mình và Bạn/Anh/Chị.
- Luôn xin lỗi nếu khách hàng gặp trải nghiệm không tốt.
- Nếu khách hỏi đổi trả: Báo rằng công ty có chính sách 1 đổi 1 trong 7 ngày.
- Giọng điệu: Chuyên nghiệp, đồng cảm và ngắn gọn.
- Luôn ký tên ở cuối là: "Trợ lý AI - Công ty ABC".
"""

# Khởi tạo mô hình AI với hướng dẫn trên
model = genai.GenerativeModel(
    model_name="gemini-flash-latest",
    system_instruction=he_thong_huong_dan
)

# 3. Hàm xử lý cốt lõi của Agent
def tu_dong_tra_loi(noidung_email_den):
    print("🤖 Agent đang đọc email và suy nghĩ câu trả lời...")
    # Gọi AI để sinh câu trả lời dựa trên email đến
    response = model.generate_content(noidung_email_den)
    return response.text

# ==========================================
# CHẠY THỬ NGHIỆM (MÔ PHỎNG)
# ==========================================

# Đây là email giả lập mà khách hàng gửi tới
email_khach_hang = """
Chào shop,
Tôi mới mua cái tai nghe bluetooth của shop hôm qua nhưng về sạc mãi không vào pin, bật không lên nguồn.
Giờ tôi muốn đổi cái khác thì làm thế nào?
Mong nhận được phản hồi sớm.
"""

print("--- 📩 EMAIL KHÁCH HÀNG GỬI ĐẾN ---")
print(email_khach_hang)
print("\n" + "="*40 + "\n")

# Đưa email cho Agent xử lý
cau_tra_loi = tu_dong_tra_loi(email_khach_hang)

print("\n--- 📤 KẾT QUẢ AI AGENT SOẠN THẢO ---")
print(cau_tra_loi)