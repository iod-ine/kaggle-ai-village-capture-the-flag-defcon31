import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE

data = np.load("data/raw/cluster2/data.npz")

tokens = data["tokens"]
points = data["points"]

model = TSNE()
lowdim = model.fit_transform(points)

fig, ax = plt.subplots(figsize=(16, 12))
aa = ax.scatter(lowdim[:, 0], lowdim[:, 1], marker="")

for token, (x, y) in zip(tokens, lowdim):
    ax.text(x, y, token, size="medium", fontfamily="serif")

plt.show()
