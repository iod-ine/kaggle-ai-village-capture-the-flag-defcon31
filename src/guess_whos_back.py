import matplotlib.pyplot as plt
import numpy as np

Xsub = np.load("data/raw/terrance/terrence.npz")["arr_0"]
plt.figure(figsize=(12, 12))
plt.imshow(Xsub, cmap="hot")
plt.show()
