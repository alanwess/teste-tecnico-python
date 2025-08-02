from transformers import pipeline
import torch

qa_pipeline = pipeline(
    "question-answering",
    model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
    revision="main",
    device=0 if torch.cuda.is_available() else -1
)

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    revision="main",
    device=0 if torch.cuda.is_available() else -1
)