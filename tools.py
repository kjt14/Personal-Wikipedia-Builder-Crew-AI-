# tools.py

def data_extractor_func(topic: str) -> str:
    return f"This is raw data for the topic: {topic}"

def summarizer_func(data: str) -> str:
    return f"Summary of data: {data[:50]}..."

def formatter_func(summary: str) -> str:
    return f"== Wikipedia Article ==\n\n{summary}"
