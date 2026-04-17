import os
from datetime import datetime

LOG_DIR = "logs"


def get_log_file():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    date_str = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(LOG_DIR, f"chat_logs_{date_str}.txt")


def log_chat(query: str, result: dict):
    """
    result = {
        "answer": str,
        "sources": list,
        "chunks": list,
        "scores": list (optional),
        "latency": float (optional)
    }
    """

    log_file = get_log_file()

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"\n{'='*60}\n")
        f.write(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        f.write(f"\nQuery:\n{query}\n")

        f.write(f"\nAnswer:\n{result.get('answer')}\n")

        sources = result.get("sources", [])
        f.write(f"\nSources:\n{sources}\n")

        chunks = result.get("chunks", [])[:3]
        f.write("\nTop Chunks:\n")
        for i, chunk in enumerate(chunks):
            f.write(f"\n--- Chunk {i+1} ---\n")
            f.write(chunk[:300] + "\n")

        scores = result.get("scores")
        if scores:
            f.write(f"\nScores:\n{scores}\n")

        latency = result.get("latency")
        if latency:
            f.write(f"\nLatency: {latency:.2f}s\n")