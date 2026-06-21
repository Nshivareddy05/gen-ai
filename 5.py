!pip install gensim nltk --quiet

import nltk
from gensim.models import Word2Vec
from nltk.corpus import brown

nltk.download('brown', quiet=True)
model = Word2Vec([[w.lower() for w in s] for s in brown.sents()], vector_size=100, window=5, min_count=2)

seed = input("Enter a seed word: ").lower()

if seed in model.wv:
    words = [w for w, _ in model.wv.most_similar(seed, topn=5)]
    print(f"\nOnce upon a time, a {seed} met a {words[0]} and {words[1]}.")
    print(f"They explored {words[2]} places, stayed {words[3]}, and realized {words[4]} is joy.")
else:
    print("Word not found.")
