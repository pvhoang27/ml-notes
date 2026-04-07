import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. IMPORT KIỂU MỚI (LCEL) - Không gọi đến thư mục bị lỗi langchain.chains
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 2. Tải API Key
load_dotenv() 

# 3. Tải và chia nhỏ tài liệu
loader = PyPDFLoader("tai_lieu_cua_toi.pdf") 
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

# 4. Tạo Vector Database 
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 5. Khởi tạo LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# 6. Tạo Prompt
system_prompt = (
    "Bạn là một trợ lý ảo hữu ích. Sử dụng các đoạn thông tin được cung cấp dưới đây "
    "để trả lời câu hỏi của người dùng. Nếu bạn không biết câu trả lời, hãy nói là bạn không biết.\n\n"
    "Thông tin tài liệu:\n{context}"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

# Hàm gom các đoạn tài liệu tìm được thành một văn bản dài
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# 7. TẠO RAG BẰNG LCEL (Chuẩn mới, né được lỗi thư viện cũ)
rag_chain = (
    {"context": retriever | format_docs, "input": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 8. Vòng lặp chat
print("Chatbot (Gemini LCEL) đã sẵn sàng! Gõ 'thoat' để dừng.")
while True:
    user_query = input("\nBạn: ")
    if user_query.lower() == 'thoat':
        break
        
    # Kiểu gọi mới chỉ cần truyền trực tiếp câu hỏi vào
    response = rag_chain.invoke(user_query)
    
    # Kết quả trả về đã là dạng text thuần (do đã qua StrOutputParser)
    print("\nBot:", response)