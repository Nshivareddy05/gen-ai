!pip install gensim transformers torch --quiet

from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
from transformers import pipeline

corpus = ["Artificial intelligence improves automation", "Machine learning learns from data", "Deep learning uses neural networks", "AI helps in robotics"]
model = Word2Vec([simple_preprocess(s) for s in corpus], vector_size=100, window=5, min_count=1)

similar = [w for w, _ in model.wv.most_similar("ai", topn=2)]
prompt1 = "Explain the benefits of AI in healthcare."
prompt2 = f"Explain the benefits of AI, {similar[0]}, and {similar[1]} in healthcare."

generator = pipeline("text-generation", model="gpt2")
print("Original Output:\n", generator(prompt1, max_length=30)[0]['generated_text'])
print("\nEnriched Output:\n", generator(prompt2, max_length=30)[0]['generated_text'])
