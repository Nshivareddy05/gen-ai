!pip install gensim scikit-learn matplotlib --quiet

import gensim.downloader as api
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

model = api.load("glove-wiki-gigaword-100")
tech_words = ["computer", "software", "hardware", "internet", "network", "database", "algorithm", "python", "cloud", "security"]

valid_words = [w for w in tech_words if w in model]
reduced = PCA(n_components=2).fit_transform(np.array([model[w] for w in valid_words]))

plt.figure(figsize=(8, 6))
plt.scatter(reduced[:, 0], reduced[:, 1], color='blue')
for i, w in enumerate(valid_words):
    plt.annotate(w, (reduced[i, 0], reduced[i, 1]))
plt.show()

print("Similarity (internet, network):", round(model.similarity("internet", "network"), 4))
print("Similar to 'cloud':", [w for w, _ in model.most_similar("cloud", topn=3)])
