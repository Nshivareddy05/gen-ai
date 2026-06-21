!pip install transformers torch --quiet

from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = pipeline("sentiment-analysis")

    def analyze(self, texts):
        for text, res in zip(texts, self.analyzer(texts)):
            print(f"[{res['label']}] ({res['score']:.2f}) : {text}")

sentences = [
    "I absolutely love this product!",
    "This is the worst experience ever.",
    "The service was okay, nothing special."
]

SentimentAnalyzer().analyze(sentences)
