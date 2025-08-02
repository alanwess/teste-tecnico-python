from datetime import datetime
from typing import Optional

def build_log_entry(request_id: str, user_id: str, query: Optional[str], result: dict):
    return {
        "request_id": request_id,
        "user_id": user_id,
        "timestamp": datetime.utcnow(),
        "query": query,
        "result": result
    }