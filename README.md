# Telecom Support Chatbot

The Telecom Support Chatbot is a locally running, Retrieval-Augmented Generation (RAG) application that answers user queries related to telecom support — including call/data/SMS plans, device configuration, troubleshooting, and more. The system utilizes FAISS for vector similarity search and the Phi-3 Mini model running via Ollama for generating intelligent responses.

## Demo

> Ask questions like:
> - "What are the latest call packages for Telenor?"
> - "How to troubleshoot network issues?"
> - "Tell me the data offers for Jazz."

## Features

- Local LLM integration using Ollama with Phi-3 Mini
- FAISS vector store for fast similarity search
- HuggingFace sentence embeddings (`all-MiniLM-L6-v2`)
- Streamlit web UI for user interaction
- Supports querying over multiple PDF documents
- Stateless, real-time question answering pipeline

## Tech Stack

| Component        | Technology Used                 |
|------------------|---------------------------------|
| Language Model   | Phi-3 Mini (via Ollama)         |
| Vector Database  | FAISS                           |
| Embeddings       | HuggingFace Transformers        |
| Framework        | LangChain                       |
| Frontend         | Streamlit                       |
| File Handling    | PyMuPDF (in ingestion phase)    |

## File Structure

<img width="399" height="93" alt="{D53124E2-A351-4733-8AE1-D96476AA6714}" src="https://github.com/user-attachments/assets/38dc69f2-ea40-416f-8bb8-54cef56b7452" />


Setup Instructions
Install Ollama and pull Phi-3 Mini


ollama pull phi3:mini
Install Python dependencies


pip install -r requirements.txt
Run the Streamlit App


streamlit run app.py
Ensure the vectorstore/ folder is already generated using the ingestion step. If not, use a document processing script to convert your PDFs into a FAISS index.

Future Work:

1. Add support for voice-to-text input and TTS output

2. Integrate real-time telecom APIs for dynamic offer retrieval

3. Add memory for multi-turn contextual chat

4. Implement user feedback loop for improving chatbot performance

5. Deploy as a containerized app using Docker for portability

License:

This project is intended for educational and non-commercial use only.
