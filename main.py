# -------------------- IMPORTS --------------------
from fastapi import FastAPI, UploadFile, BackgroundTasks
from pydantic import BaseModel
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import PyPDF2
import io
import time

# -------------------- APP --------------------
app = FastAPI()

# -------------------- MODEL --------------------
# Converts text into vectors
model = SentenceTransformer("all-MiniLM-L6-v2")

# -------------------- VECTOR DATABASE --------------------
index = faiss.IndexFlatL2(384)  # 384 = vector size
id_to_text = {}
current_id = 0


# -------------------- CHUNK FUNCTION --------------------
def chunk_text(text):
    chunks = []
    chunk_size = 500
    overlap = 50

    for i in range(0, len(text), chunk_size - overlap):
        part = text[i:i + chunk_size]
        chunks.append(part)

    return chunks


# -------------------- EXTRACT TEXT --------------------
def extract_text(file: UploadFile):
    if file.filename.endswith(".pdf"):
        pdf = PyPDF2.PdfReader(io.BytesIO(file.file.read()))
        text = ""

        for page in pdf.pages:
            content = page.extract_text()
            if content:
                text += content

        return text

    elif file.filename.endswith(".txt"):
        return file.file.read().decode("utf-8")

    else:
        return ""


# -------------------- PROCESS DOCUMENT --------------------
def process_file(file: UploadFile):
    global current_id

    text = extract_text(file)

    if text == "":
        return

    chunks = chunk_text(text)

    embeddings = model.encode(chunks)

    index.add(np.array(embeddings))

    for chunk in chunks:
        id_to_text[current_id] = chunk
        current_id += 1


# -------------------- UPLOAD API --------------------
@app.post("/upload")
async def upload(file: UploadFile):
    process_file(file)
    return {"message": "File uploaded and processed"}


# -------------------- QUERY MODEL --------------------
class Question(BaseModel):
    question: str


# -------------------- QUERY API --------------------
@app.post("/query")
def query(data: Question):

    if index.ntotal == 0:
        return {"answer": "No document uploaded yet"}

    start = time.time()

    # Convert question to vector
    query_vector = model.encode([data.question])

    # Search similar chunks
    D, I = index.search(np.array(query_vector), k=3)

    results = []

    for i in I[0]:
        if i in id_to_text:
            results.append(id_to_text[i])

    context = " ".join(results)

    end = time.time()

    return {
        "question": data.question,
        "answer": context[:300],
        "time_taken": round(end - start, 3)
    }


# -------------------- HOME --------------------
@app.get("/")
def home():
    return {"message": "RAG system running"}