from __future__ import annotations

import os
from functools import lru_cache
from typing import List

from openai import OpenAI
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter

# Keep these consistent with your Qdrant collection configuration
EMBED_MODEL = "text-embedding-3-large"  # 3072 dims
EMBED_DIM = 3072

# Tune chunking as needed for your PDFs
splitter = SentenceSplitter(chunk_size=2000, chunk_overlap=250)


@lru_cache(maxsize=1)
def get_openai_client() -> OpenAI:
    """
    Lazily construct the OpenAI client from the OPENAI_API_KEY env var.
    Make sure your app loads .env BEFORE importing this module
    (or start the process with: `uv run --env-file .env ...`).
    """
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise RuntimeError(
            "OPENAI_API_KEY not set. Load your .env early in app startup or run with "
            "`uv run --env-file .env ...`"
        )
    return OpenAI(api_key=key)


def load_and_chunk_pdf(path: str) -> List[str]:
    """
    Load a PDF file and split it into text chunks suitable for embedding.
    """
    docs = PDFReader().load_data(file=path)  # type: ignore # path must be a string
    texts = [d.text for d in docs if getattr(d, "text", None)]
    chunks: List[str] = []
    for t in texts:
        chunks.extend(splitter.split_text(t))
    return chunks


def embed_texts(texts: List[str]) -> List[List[float]]:
    """
    Embed a list of strings into vectors using OpenAI embeddings.
    Returns a list of 3072-d float vectors (for text-embedding-3-large).
    """
    if not texts:
        return []

    client = get_openai_client()
    resp = client.embeddings.create(model=EMBED_MODEL, input=texts)
    return [d.embedding for d in resp.data]