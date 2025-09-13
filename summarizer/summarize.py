import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

import time
from google.genai.errors import ServerError

def summarize_chunk(chunk: str) -> str:
    """Summarizes a single chunk with automatic retry on 503."""
    max_retries = 5
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Summarize the following text in 3-4 bullet points:\n\n{chunk}"
            )
            return response.text.strip()
        except ServerError as e:
            print(f"Server busy (attempt {attempt+1}/{max_retries}), retrying in {2 ** attempt} seconds...")
            time.sleep(2 ** attempt)
    raise Exception("Failed after multiple retries due to server overload")

def consolidate_summaries(chunk_summaries: list[str]) -> str:
    """Consolidates multiple chunk summaries into a single executive summary."""
    joined = "\n".join(chunk_summaries)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Combine these chunk summaries into a 4-5 sentence executive summary with key action items:\n\n{joined}",
    )
    return response.text.strip()

def summarize_pipeline(text: str) -> tuple[str, list[str]]:
    """Full pipeline: text → chunks → chunk summaries → consolidated summary."""
    from .chunker import chunk_text

    chunks = chunk_text(text, chunk_size=800, overlap=150)
    chunk_summaries = [summarize_chunk(c) for c in chunks]
    final_summary = consolidate_summaries(chunk_summaries)
    return final_summary, chunk_summaries
