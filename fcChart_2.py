import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
scores = np.random.normal(loc=7, scale=1.5, size=100)
scores = np.clip(scores, 0, 10)

counts, bin_edges = np.histogram(scores, bins=10)
cdf = np.cumsum(counts) / np.sum(counts)

plt.plot(bin_edges[1:], cdf, marker="o", color="red")
plt.title("Đường tần suất tích lũy (CDF)")
plt.xlabel("Điểm")
plt.ylabel("Tỷ lệ tích lũy")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
