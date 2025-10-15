# RAG App

A Retrieval-Augmented Generation (RAG) application that allows you to upload PDF documents and ask questions about their content using AI. The app combines vector search with large language models to provide accurate, context-aware answers.

## Features

- **PDF Ingestion**: Upload and process PDF documents for searchable content
- **Vector Storage**: Uses Qdrant vector database for efficient similarity search
- **AI-Powered Q&A**: Leverages OpenAI GPT models for intelligent question answering
- **Workflow Orchestration**: Built with Inngest for reliable, observable workflows
- **Interactive UI**: Streamlit-based web interface for easy document upload and querying
- **Chunk-based Retrieval**: Smart text chunking with configurable overlap for better context

## Architecture

- **FastAPI Backend**: RESTful API with Inngest workflow integration
- **Streamlit Frontend**: User-friendly interface for PDF upload and querying
- **Qdrant Vector DB**: High-performance vector storage and similarity search
- **OpenAI Embeddings**: Text-embedding-3-large model for vector generation
- **GPT-4o-mini**: Language model for generating answers from retrieved context

## Prerequisites

- Python 3.12+
- Docker (for Qdrant vector database)
- OpenAI API key

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd RAGApp
   ```

2. **Install dependencies**:
   ```bash
   uv sync
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

4. **Start Qdrant vector database**:
   ```bash
   docker run -p 6333:6333 qdrant/qdrant
   ```

## Usage

### Starting the Application

1. **Start the FastAPI backend**:
   ```bash
   uv run uvicorn main:app --reload
   ```

2. **Start the Streamlit frontend** (in another terminal):
   ```bash
   uv run streamlit run streamlit_app.py
   ```

3. **Access the application**:
   - Streamlit UI: http://localhost:8501
   - FastAPI docs: http://localhost:8000/docs

### Using the RAG System

1. **Upload a PDF**: Use the Streamlit interface to upload PDF documents
2. **Wait for Processing**: The system will chunk the text and create embeddings
3. **Ask Questions**: Query your documents using natural language
4. **Get AI Answers**: Receive contextual answers with source references

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key for embeddings and chat completion
- `INNGEST_API_BASE`: Inngest API endpoint (defaults to local dev server)

### Customizable Parameters

- **Chunk Size**: Modify `chunk_size` in `data_loader.py` (default: 2000)
- **Chunk Overlap**: Adjust `chunk_overlap` in `data_loader.py` (default: 250)
- **Embedding Model**: Change `EMBED_MODEL` in `data_loader.py` (default: text-embedding-3-large)
- **Vector Dimensions**: Update `EMBED_DIM` to match your embedding model
- **Retrieval Count**: Adjust `top_k` parameter for number of chunks retrieved

## Project Structure

```
RAGApp/
├── main.py              # FastAPI app with Inngest workflows
├── streamlit_app.py     # Streamlit web interface
├── data_loader.py       # PDF processing and embedding logic
├── vector_db.py         # Qdrant vector database operations
├── custom_types.py      # Pydantic models for type safety
├── pyproject.toml       # Project dependencies and metadata
├── .env                 # Environment variables (not in repo)
├── uploads/             # Directory for uploaded PDFs
└── qdrant_storage/      # Qdrant database files
```

## API Endpoints

### Inngest Workflows

- **POST /api/inngest**: Inngest webhook endpoint
- **RAG: Ingest PDF**: Processes uploaded PDFs and stores embeddings
- **RAG: Query PDF**: Handles question answering with retrieved context


## Troubleshooting

### Common Issues

1. **Qdrant Connection Error**: Ensure Docker container is running on port 6333
2. **OpenAI API Error**: Verify your API key is set correctly in `.env`
3. **PDF Processing Error**: Check that uploaded files are valid PDFs
4. **Memory Issues**: For large PDFs, consider reducing chunk size or increasing system memory

### Logs and Monitoring

- Check Inngest dashboard for workflow execution details
- FastAPI logs available at the uvicorn console
- Streamlit logs visible in the browser console

## Acknowledgments

- [Qdrant](https://qdrant.tech/) for vector database
- [OpenAI](https://openai.com/) for embeddings and language models
- [Inngest](https://inngest.com/) for workflow orchestration
- [Streamlit](https://streamlit.io/) for the web interface
- [LlamaIndex](https://www.llamaindex.ai/) for document processing utilities