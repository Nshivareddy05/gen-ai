!pip install gensim --quiet

from gensim.models import Word2Vec
from gensim.utils import simple_preprocess

corpus = [
    "The doctor prescribed antibiotics for the infection",
    "The patient was diagnosed with diabetes and hypertension",
    "Surgery was performed to remove the tumor",
    "The nurse monitored the patient's vital signs",
    "Cancer treatment includes chemotherapy and radiation therapy"
]

processed = [simple_preprocess(s) for s in corpus]
model = Word2Vec(processed, vector_size=100, window=5, min_count=1)

print("Similar to 'doctor':", [w for w, _ in model.wv.most_similar("doctor", topn=3)])
print("Similarity (cancer, tumor):", round(model.wv.similarity("cancer", "tumor"), 4))
