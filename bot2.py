import os
import google.generativeai as genai
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# 1. Tải API Key 
load_dotenv() 
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# 2. Khởi tạo Model 
model = genai.GenerativeModel('gemini-flash-latest')

# 3. Cấu hình Embeddings và Thư mục lưu DB
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
persist_directory = "my_vector_db" # Tên thư mục sẽ được tạo ra để chứa DB trên ổ cứng

# 4. LOGIC TỐI ƯU: Có DB rồi thì load, chưa có thì mới tạo
if os.path.exists(persist_directory):
    print("⚡ Đã tìm thấy Vector Database. Đang tải từ ổ cứng lên (Bỏ qua bước đọc PDF)...")
    vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
else:
    print("⏳ Lần đầu chạy: Đang đọc PDF, chia nhỏ và lưu Database xuống ổ cứng...")
    loader = PyPDFLoader("tai_lieu_cua_toi.pdf") 
    docs = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    
    # Lệnh này vừa tạo DB vừa lưu thẳng xuống thư mục persist_directory
    vectorstore = Chroma.from_documents(
        documents=splits, 
        embedding=embeddings, 
        persist_directory=persist_directory 
    )

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 5. Vòng lặp chat RAG
print("Chatbot (Gemini Native) đã sẵn sàng! Gõ 'thoat' để dừng.")
while True:
    user_query = input("\nBạn: ")
    if user_query.lower() == 'thoat':
        break
        
    # Bước A: Tìm kiếm tài liệu
    relevant_docs = retriever.invoke(user_query)
    
    # Bước B: Gom text
    context = "\n\n".join(doc.page_content for doc in relevant_docs)
    
    # Bước C: Ép Prompt
    prompt = f"""Bạn là một trợ lý ảo hữu ích. Sử dụng các đoạn thông tin được cung cấp dưới đây để trả lời câu hỏi của người dùng. Nếu bạn không biết câu trả lời, hãy nói là bạn không biết.
    
    Thông tin tài liệu:
    {context}
    
    Câu hỏi của người dùng: {user_query}
    """
    
    # Bước D: Gọi API
    try:
        response = model.generate_content(prompt)
        print("\nBot:", response.text)
    except Exception as e:
        print("\nBot: Xin lỗi, có lỗi xảy ra khi gọi API -", e)