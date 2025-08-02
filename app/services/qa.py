from typing import List
from app.core.pipeline import qa_pipeline

def answer_query(texts: List[str], query: str) -> List[dict]:
    results = []
    for idx, text in enumerate(texts):
        result = qa_pipeline(question=query, context=text)
        results.append({
            "cv_index": idx,
            "response": result['answer'],
            "score": result['score']
        })
    return sorted(results, key=lambda x: x['score'], reverse=True)