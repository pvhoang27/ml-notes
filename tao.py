from fpdf import FPDF

# 1. Nội dung tiếng Việt không dấu để không cần tải font
content = [
    {
        "title": "Chuong 1: Gioi thieu chung ve TechFuture JSC",
        "body": "Cong ty Co phan Cong nghe Tuong Lai (TechFuture JSC) la doanh nghiep hang dau trong linh vuc AI tai Viet Nam.\n\nTru so chinh dat tai Toa nha Innovation, Cau Giay, Ha Noi."
    },
    {
        "title": "Chuong 2: Lich su va San pham",
        "body": "Thanh lap nam 2018.\n\nSan pham chinh:\n- VisionAI: He thong camera thong minh.\n- SpeakToMe: Tro ly ao AI."
    }
]

# 2. Tạo PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# 3. Ghi nội dung (Dùng font Arial mặc định, không cần tải)
for section in content:
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, section["title"], ln=True, align="C")
    pdf.ln(10)
    
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8, section["body"])

# 4. Xuất file
pdf.output("tai_lieu_cua_toi.pdf")
print("Đã tạo xong file: tai_lieu_cua_toi.pdf (Bản không dấu). Bạn chạy file rag_bot.py đi!")