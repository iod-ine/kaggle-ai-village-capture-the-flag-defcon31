import matplotlib.pyplot as plt
import numpy as np

XX = np.load("data/raw/terrance/terrence.npz")["arr_0"]

two_hundred_and_one = XX.copy()
two_hundred_and_one = two_hundred_and_one.reshape(-1)
two_hundred_and_one[two_hundred_and_one != 201] = 0
two_hundred_and_one = two_hundred_and_one.reshape(XX.shape)

plt.figure(figsize=(12, 12))
plt.imshow(XX, cmap="hot")
plt.show()

plt.figure(figsize=(12, 12))
plt.imshow(two_hundred_and_one, cmap="hot")
plt.show()
