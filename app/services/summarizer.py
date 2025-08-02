from app.core.pipeline import summarizer

def summarize_text(text: str) -> str:
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    return " ".join(summarizer(chunk)[0]['summary_text'] for chunk in chunks if chunk.strip())