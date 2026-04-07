"""
=== BAI PHONG VAN GENAI - CODE TREN MAY ===

De bai:
  User gui file "report.docx" va yeu cau:
  "Trich xuat tat ca bang doanh thu trong file nay, tao file Excel, roi gui qua email cho sep toi"

Yeu cau:
  1. Thiet ke va code cac tool can thiet cho agent
  2. Xay dung agent loop de agent tu dong xu ly yeu cau tren
  3. Agent phai biet hoi lai user khi thieu thong tin
  4. Su dung OpenAI API (function calling)

Tieu chi danh gia:
  - Thiet ke tool hop ly (du tool, khong thua)          [3 diem]
  - Agent loop dung (Thought -> Action -> Observation)   [3 diem]
  - Xu ly thieu thong tin (hoi lai user)                 [2 diem]
  - Code chay duoc, cho ket qua dung                     [2 diem]

Luu y:
  - File report.docx da duoc cung cap san
  - Ham send_email chi can mo phong bang print, KHONG can gui email that
  - OPENAI_API_KEY da duoc set san trong moi truong
  - Thoi gian: 15 phut

Cai dat thu vien:
  pip install openai python-docx openpyxl

Chay: python starter.py
"""


import os
from openai import OpenAI

client = OpenAI()


# Viet code cua ban o day



if __name__ == "__main__":
    user_request = (
        'Trich xuat tat ca bang doanh thu trong file "report.docx", '
        'tao file Excel, roi gui qua email cho sep toi.'
    )
    print(f"User: {user_request}\n")
    # Goi agent cua ban o day