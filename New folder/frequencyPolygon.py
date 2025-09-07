import numpy as np
import matplotlib.pyplot as plt
# Dữ liệu: Điểm số của học sinh
np.random.seed(42)
scores = np.random.randint(40, 100, size=200)   # điểm từ 40 đến 100
# Tạo histogram và frequency polygon
counts, bin_edges = np.histogram(scores, bins=10)   # chia 10 lớp
bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])   # trung điểm lớp
plt.figure(figsize=(8,5))
# Histogram để so sánh
plt.hist(scores, bins=10, color="skyblue", edgecolor="black", alpha=0.6, label="Histogram")
# Frequency Polygon
plt.plot(bin_centers, counts, marker="o", linestyle="-", color="red", label="Frequency Polygon")
plt.title("Biểu đồ Frequency Polygon")
plt.xlabel("Điểm số")
plt.ylabel("Tần số")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()