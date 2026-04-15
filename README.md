# RAG-Based Question Answering System

## 📌 Overview

This project is a simple implementation of a Retrieval-Augmented Generation (RAG) system built using FastAPI.
It allows users to upload documents and ask questions based on the content of those documents.

The system does not rely on general knowledge. Instead, it retrieves relevant information from the uploaded document and uses that as the basis for answering queries.

---

## 🚀 Features

* Upload documents (PDF and TXT supported)
* Extract and process document text
* Chunk text into smaller segments
* Generate embeddings using Sentence Transformers
* Store embeddings in FAISS (vector database)
* Retrieve relevant chunks using similarity search
* Answer questions based on retrieved content
* Fast API with simple endpoints

---

## 🧠 How It Works

### Step 1: Upload Document

The user uploads a document using the `/upload` endpoint.

### Step 2: Text Extraction

* PDF files are processed using PyPDF2
* TXT files are read directly

### Step 3: Chunking

The text is split into smaller chunks:

* Chunk size: 500 characters
* Overlap: 50 characters

This improves retrieval accuracy and preserves context.

### Step 4: Embedding Generation

Each chunk is converted into a numerical vector using the model:
`all-MiniLM-L6-v2`

### Step 5: Storage

All embeddings are stored in FAISS for fast similarity search.

### Step 6: Query Processing

* User sends a question via `/query`
* The question is converted into a vector
* FAISS retrieves the most similar chunks

### Step 7: Answer Generation

The retrieved chunks are combined and returned as the answer.

---

## 📊 Design Decisions

### Chunk Size

A chunk size of 500 with 50 overlap was chosen to balance:

* Context preservation
* Retrieval precision

### Retrieval Failure Case

For vague queries like:
"What is this about?"

The system may retrieve less relevant chunks due to lack of clear semantic meaning.

### Metric Tracked

Latency (response time) was tracked to measure performance.
Typical response time: 0.2–0.5 seconds.

---

## ⚙️ Setup Instructions

### 1. Clone Repository

git clone <your-repo-link>
cd rag-system

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Run Server

uvicorn main:app --reload

### 4. Open in Browser

http://127.0.0.1:8000/docs

---

## 🧪 Usage

### Upload Document

* Endpoint: POST `/upload`
* Upload a PDF or TXT file

### Ask Question

* Endpoint: POST `/query`

Example:
{
"question": "What is the document about?"
}

---

## 📁 Project Structure

rag-system/
│
├── main.py
├── requirements.txt
└── README.md

---

## ⚠️ Limitations

* Only one document is handled at a time (previous data is cleared)
* No advanced LLM used for answer generation
* Depends on quality of extracted text

---

## 🔮 Future Improvements

* Support multiple documents
* Integrate LLM for better answers
* Improve UI/UX
* Add document filtering

---

## 🎥 Demo

https://drive.google.com/file/d/1g4H4gnvXRp9kOGqCzoTRz7VdUxAwQn8m/view?usp=sharing

---

## 📊 Architecture Diagram

https://drive.google.com/file/d/1_aMmtZnVXVToNW5YGOSIty8wt-5Sv8H_/view?usp=sharing

---

## 🙌 Conclusion

This project demonstrates how a RAG pipeline works using embeddings, vector search, and retrieval-based answering.

It provides a strong foundation for building more advanced AI-powered systems.
