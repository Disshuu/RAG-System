import streamlit as st
import requests
import time

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="RAG Question Answering System",
    page_icon="🤖",
    layout="centered"
)

# -------------------- TITLE --------------------
st.title("🤖 RAG Based Question Answering System")
st.write("Upload a PDF or TXT document and ask questions!")

# -------------------- FILE UPLOAD --------------------
uploaded_file = st.file_uploader(
    "📄 Upload your Document",
    type=["pdf", "txt"]
)

if uploaded_file is not None:
    with st.spinner("Processing document..."):
        files = {"file": (uploaded_file.name,
                          uploaded_file,
                          "application/octet-stream")}
        try:
            response = requests.post(
                "http://localhost:8000/upload",
                files=files
            )
            if response.status_code == 200:
                st.success("✅ Document uploaded successfully!")
            else:
                st.error("❌ Upload failed!")
        except:
            st.error("❌ Server not running!")

# -------------------- QUESTION INPUT --------------------
st.markdown("---")
question = st.text_input("❓ Ask a Question about your document")

if st.button("Get Answer 🚀"):
    if question:
        with st.spinner("Searching for answer..."):
            try:
                response = requests.post(
                    "http://localhost:8000/query",
                    json={"question": question}
                )
                if response.status_code == 200:
                    data = response.json()
                    st.markdown("### 💡 Answer:")
                    st.success(data["answer"])
                    st.caption(
                        f"⏱️ Time taken: {data['time_taken']} seconds"
                    )
                else:
                    st.error("❌ Query failed!")
            except:
                st.error("❌ Server not running!")
    else:
        st.warning("⚠️ Please enter a question!")
