# 🤖 RAG-Based Question Answering System

## 📌 Overview

This project is a Retrieval-Augmented Generation (RAG) based Question Answering System built using Streamlit, FAISS, and Sentence Transformers.

The application allows users to upload PDF or TXT documents and ask questions based on the uploaded content. Instead of relying on general AI knowledge, the system retrieves contextually relevant information from the uploaded document using semantic similarity search.

The project demonstrates how modern AI retrieval pipelines work using embeddings, vector databases, and semantic search techniques.

---

## 🚀 Features

* Upload PDF and TXT documents
* Extract and process document text
* Chunk large text into smaller segments
* Generate embeddings using Sentence Transformers
* Store embeddings in FAISS vector database
* Perform semantic similarity search
* Retrieve relevant chunks for answering questions
* Interactive Streamlit UI
* Real-time document-based question answering
* Deployed on Hugging Face Spaces using Docker

---

## 🧠 Tech Stack

* Python
* Streamlit
* Sentence Transformers
* FAISS
* NumPy
* PyPDF2
* Docker
* Hugging Face Spaces

---

## ⚙️ How It Works

### 1. Document Upload

Users upload a PDF or TXT document through the Streamlit interface.

### 2. Text Extraction

* PDF files are processed using PyPDF2
* TXT files are read directly

### 3. Text Chunking

The extracted text is divided into smaller chunks.

* Chunk Size: 500 characters
* Overlap: 50 characters

This helps preserve context and improves retrieval quality.

### 4. Embedding Generation

Each text chunk is converted into vector embeddings using:

all-MiniLM-L6-v2

### 5. Vector Storage

The embeddings are stored inside a FAISS vector database for efficient similarity search.

### 6. Question Processing

When a user asks a question:

* The question is converted into an embedding vector
* FAISS searches for the most relevant chunks
* Similar chunks are retrieved based on vector similarity

### 7. Answer Retrieval

The retrieved chunks are combined and returned as the final response.

---

## 📊 Design Decisions

### Chunk Size Selection

A chunk size of 500 with 50-character overlap was chosen to balance:

* Context preservation
* Retrieval accuracy
* Efficient vector search

### Embedding Model

The model `all-MiniLM-L6-v2` was selected because it is:

* Lightweight
* Fast
* Effective for semantic similarity tasks

### Vector Database

FAISS was used for:

* Fast similarity search
* Efficient vector indexing
* Low-latency retrieval

---

## ⚠️ Limitations

* Handles one document at a time
* Retrieval quality depends on extracted text quality
* No advanced LLM-based answer generation
* Scanned PDFs may not extract text correctly

---

## 🔮 Future Improvements

* Multi-document support
* Conversational memory
* LLM integration for better answer generation
* Chat-style UI
* Source citation support
* OCR support for scanned PDFs

---

## 🌐 Live Demo

Deployed on Hugging Face Spaces:

https://huggingface.co/spaces/Dishu27/RAG-QA-System

---

## 🎥 Demo Video

https://drive.google.com/file/d/1geMWwSyB7VWaimCE0jQs2urfS5eeAD98/view?usp=sharing

---

## 📊 Architecture Diagram

https://drive.google.com/file/d/1_aMmtZnVXVToNW5YGOSIty8wt-5Sv8H_/view?usp=sharing

---

## ⚙️ Setup Instructions

### 1. Clone Repository

git clone <your-repository-link>

cd rag-system

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Run Application

streamlit run app.py

---

## 📁 Project Structure

rag-system/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .streamlit/
└── config.toml

---

## 💡 Example Workflow

1. Upload a PDF or TXT document
2. Ask questions related to the document
3. System retrieves semantically relevant content
4. Relevant answer is displayed instantly

---

## 🙌 Conclusion

This project demonstrates the complete workflow of a Retrieval-Augmented Generation (RAG) pipeline using embeddings, semantic search, and vector databases.

It provides a strong foundation for building scalable AI-powered document intelligence systems and real-world semantic retrieval applications.
