from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization", model="t5-small")

def summarize_text(text):
    summary = summarizer(text, max_length=60, min_length=25, do_sample=False)[0]['summary_text']
    word_count = len(summary.split())
    return summary, f"Word Count: {word_count}"
