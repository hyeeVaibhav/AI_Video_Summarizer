def chunk_text(text: str, chunk_size: int = 2000, overlap: int = 200) -> list:
    chunks = []
    start = 0
    text_length = len(text)
    
    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap # Keeps context between chunks
        
    return chunks

def chunked_summary(text: str, summarization_fn, max_chunk_size: int = 2000) -> str:
    text_chunks = chunk_text(text, chunk_size=max_chunk_size)
    partial_summaries = []
    
    for chunk in text_chunks:
        partial_summaries.append(summarization_fn(chunk))
        
    return " ".join(partial_summaries)