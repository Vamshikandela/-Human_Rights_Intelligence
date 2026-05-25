import fitz
import os

from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings


def extract_text_from_pdf(pdf_path: str):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    return text


def build_index_from_pdf(
    pdf_path: str,
    persist_dir: str = "rag_faiss_store"
):

    full_text = extract_text_from_pdf(pdf_path)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=350,
        chunk_overlap=100
    )

    documents = splitter.split_documents(
        [Document(page_content=full_text)]
    )

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(documents, embeddings)

    os.makedirs(persist_dir, exist_ok=True)

    db.save_local(persist_dir)