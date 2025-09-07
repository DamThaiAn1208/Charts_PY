import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
scores = np.random.normal(loc=7, scale=1.5, size=100)
scores = np.clip(scores, 0, 10)

plt.hist(scores, bins=10, cumulative=True, color="skyblue", edgecolor="black")
plt.title("Biểu đồ tần suất tích lũy điểm thi")
plt.xlabel("Điểm")
plt.ylabel("Số học sinh tích lũy")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
