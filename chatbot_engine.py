from langchain_ollama import OllamaLLM
from langchain.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
import os
import glob

# Directory paths
DATA_DIR = "data"
VECTORSTORE_DIR = "vectorstore"

# Load and split all PDF documents from the data folder
def load_documents(data_dir):
    all_docs = []
    pdf_files = glob.glob(os.path.join(data_dir, "*.pdf"))
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

    for pdf_path in pdf_files:
        loader = PyMuPDFLoader(pdf_path)
        docs = loader.load()
        chunks = splitter.split_documents(docs)
        all_docs.extend(chunks)

    return all_docs

# Create and save vectorstore
def create_vector_store(docs):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(VECTORSTORE_DIR)
    return vectorstore

# Load vectorstore or create it if missing
def get_vector_store():
    try:
        return FAISS.load_local(
            VECTORSTORE_DIR,
            HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
            allow_dangerous_deserialization=True
        )
    except Exception as e:
        print(f"[INFO] FAISS index not found or corrupted. Rebuilding... Reason: {e}")
        docs = load_documents(DATA_DIR)
        return create_vector_store(docs)

# Generate chat response
def get_chat_response(query):
    vectorstore = get_vector_store()
    retriever = vectorstore.as_retriever()
    llm = OllamaLLM(model="phi")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain.run(query)
