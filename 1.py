!pip install gensim scikit-learn matplotlib --quiet

import gensim.downloader as api
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

model = api.load("glove-wiki-gigaword-100")

print("Similarity (king, queen):", round(model.similarity("king", "queen"), 4))
print("Analogy (king - man + woman):", model.most_similar(positive=["king", "woman"], negative=["man"], topn=1)[0])

words = ["king", "queen", "man", "woman", "prince", "princess", "france", "paris", "italy", "rome"]
vectors = np.array([model[w] for w in words])
reduced = PCA(n_components=2).fit_transform(vectors)

plt.figure(figsize=(8, 6))
plt.scatter(reduced[:, 0], reduced[:, 1])
for w, (x, y) in zip(words, reduced):
    plt.text(x + 0.01, y + 0.01, w)
plt.show()
