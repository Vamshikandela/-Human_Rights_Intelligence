import streamlit as st
import os
import tempfile

from dotenv import load_dotenv

from google import genai

from rag_index_builder import build_index_from_pdf
from tools import retrieve_legal_context
import base64


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)


# STREAMLIT UI

st.set_page_config(
    page_title="Human_Rights_Intelligence",
    layout="wide"
)

st.title("⚖️Human_Rights_Intelligence")



## background image 
def set_background(image_file):

    with open(image_file, "rb") as image:

        encoded = base64.b64encode(image.read()).decode()

    page_bg = f"""
    <style>

    /* MAIN APP BACKGROUND */

    .stApp {{
        background:
            linear-gradient(
                rgba(0,0,0,0.65),
                rgba(0,0,0,0.60)
            ),
            url("data:image/jpg;base64,{encoded}");

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* TEXT COLORS */

    h1, h2, h3, h4, h5, h6, p, label {{
        color: white !important;
    }}

    /* FILE UPLOADER */

    [data-testid="stFileUploader"] {{
        background-color: rgba(25,25,25,0.75);
        padding: 20px;
        border-radius: 15px;
    }}

    /* TEXT INPUT */

    .stTextInput > div > div > input {{
        background-color: rgba(30,30,30,0.85);
        color: white;
        border-radius: 10px;
        border: 1px solid rgba(255,255,255,0.1);
    }}

    /* SAMPLE QUESTION BOX */

    .sample-box {{
        background-color: rgba(35,35,35,0.80);
        color: white;
        padding: 14px;
        border-radius: 10px;
        margin-bottom: 12px;
        border: 1px solid rgba(255,255,255,0.1);
        font-size: 16px;
    }}

    /* ANSWER BOX */

    .answer-box {{
        background-color: rgba(15,15,15,0.92);
        color: white;
        padding: 25px;
        border-radius: 15px;
        font-size: 20px;
        line-height: 1.8;
        border: 1px solid rgba(255,255,255,0.1);
        margin-top: 20px;
    }}

    /* REMOVE WHITE HEADER */

    header {{
        background-color: transparent !important;
    }}

    /* SIDEBAR */

    section[data-testid="stSidebar"] {{
        background-color: rgba(20,20,20,0.85);
    }}

    </style>
    """

    st.markdown(page_bg, unsafe_allow_html=True)


# ======================================================
# SET BACKGROUND IMAGE
# ========================================================

set_background("download.jpg")

def generate_answer(query):

    context = retrieve_legal_context(query)

    prompt= f"""
    You are an expert constitutional law professor and legal research assistant.

    Your task is to answer questions strictly using retrieved legal context.

    The retrieved documents may contain:
    - constitutional provisions
    - legal explanations
    - comparative legal tables
    - mappings between Universal Declaration of Human Rights (UDHR)
    and Indian Constitutional Articles

    Instructions:

    1. If the retrieved context contains BOTH:
    - Universal Declaration article
    - Indian Constitutional article

    then explain BOTH clearly.

    2. When tables are present:
    - read the relationship between columns carefully
    - identify corresponding legal provisions
    - explain the connection professionally

    3. Structure answers like this:

    - Universal Declaration Provision
    - Indian Constitutional Provision
    - Legal Meaning
    - Constitutional Importance

    4. Use formal legal-academic language.

    5. Do NOT give one-line answers.

    6. Do NOT hallucinate legal provisions outside retrieved context.

    7. If the question refers to a legal right,
    identify corresponding articles from both:
    - UDHR
    - Indian Constitution

    Retrieved Context:
    {context}

    Question:
    {query}

    Answer:
    """
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents=prompt
    )

    return response.text




st.markdown("""
Upload legal PDFs and ask legal questions.
The assistant answers using retrieved document context.
""")


uploaded_file = st.file_uploader(
    "Upload Legal PDF",
    type=["pdf"]
)


if uploaded_file is not None:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp_file:

        tmp_file.write(uploaded_file.read())

        tmp_pdf_path = tmp_file.name

    st.success("PDF uploaded successfully.")

    with st.spinner("Building FAISS index..."):

        build_index_from_pdf(
            tmp_pdf_path,
            persist_dir="rag_faiss_store"
        )

    st.success("Index created successfully.")

    st.markdown("---")

    
st.subheader("📚 Sample Legal Questions")

sample_questions = [
    "What is Article 14 of the Indian Constitution?",
    "Explain Article 21 and protection of life and personal liberty.",
    "What is freedom of conscience and religion?",
    "Explain Article 32 constitutional remedies.",
    "What protections exist against forced labour?",
    "Compare UDHR and Indian constitutional rights.",
    "Explain the right to work and favourable conditions of work under UDHR and the Indian Constitution.",
    "What is the right to equal pay for equal work under human rights law?",
    "Explain the right to education under the Universal Declaration of Human Rights and the Constitution of India.",
    "What is the right against arbitrary arrest and detention?",
    "Explain freedom of speech and expression."
]

left_col, right_col = st.columns(2)

mid = len(sample_questions) // 2

left_questions = sample_questions[:mid]
right_questions = sample_questions[mid:]


with left_col:

    for question in left_questions:

        st.markdown(
            f"""
            <div class="sample-box">
                {question}
            </div>
            """,
            unsafe_allow_html=True
        )


with right_col:

    for question in right_questions:

        st.markdown(
            f"""
            <div class="sample-box">
                {question}
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================
# USER INPUT
# =========================================

query = st.text_input(
    "Ask your legal question",
    placeholder="Example: Explain Article 21 under Indian Constitution"
)

if query:

    with st.spinner("Retrieving legal context and generating answer..."):

        answer = generate_answer(query)

    st.markdown("## ⚖️ Legal Answer")

    st.markdown(
        f"""
        <div class="answer-box">
            {answer}
        </div>
        """,
        unsafe_allow_html=True
    )