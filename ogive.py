import numpy as np
import matplotlib.pyplot as plt
# Dữ liệu: điểm số học sinh
np.random.seed(42)
scores = np.random.randint(40, 100, size=200)   # 200 học sinh, điểm 40-100
# Histogram để tính tần số
counts, bin_edges = np.histogram(scores, bins=10)
# Tính tần suất tích lũy
cum_counts = np.cumsum(counts)
# Trung điểm các lớp
bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])
# Vẽ biểu đồ Ogive
plt.figure(figsize=(8,5))
plt.plot(bin_centers, cum_counts, marker="o", linestyle="-", color="green", label="Ogive")
plt.title("Biểu đồ Ogive (Tần suất tích lũy)")
plt.xlabel("Điểm số")
plt.ylabel("Tần số tích lũy")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.show()