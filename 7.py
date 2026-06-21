!pip install transformers torch accelerate --quiet

from transformers import pipeline
import textwrap

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

text = "Artificial Intelligence (AI) is a rapidly evolving field of computer science that aims to create systems capable of performing tasks that typically require human intelligence. These tasks include problem-solving, learning, reasoning, perception, and language understanding. AI has been applied across various domains such as healthcare, finance, transportation, and education."

summary = summarizer(text, max_length=40, min_length=15, do_sample=False)
print("ORIGINAL:\n", textwrap.fill(text, 80))
print("\nSUMMARY:\n", textwrap.fill(summary[0]['summary_text'], 80))
