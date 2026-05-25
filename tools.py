from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


# SAME embedding model used during indexing
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS vector store
db = FAISS.load_local(
    "rag_faiss_store",
    embeddings,
    allow_dangerous_deserialization=True
)


def retrieve_legal_context(query: str) -> str:

    docs = db.similarity_search(query, k=3)

    results = []

    for doc in docs:
        results.append(doc.page_content)

    return "\n\n".join(results)