# Biểu đồ Dotplot
import numpy as np
import matplotlib.pyplot as plt

# Dữ liệu điểm số của một lớp học
np.random.seed(42)
scores = np.random.randint(5, 11, size=30)  # điểm từ 5 đến 10

# Chuẩn bị dữ liệu cho Dotplot
x = []
y = []
for value in np.unique(scores):
    count = np.sum(scores == value)   # đếm số lần xuất hiện
    x.extend([value] * count)         # giữ nguyên giá trị x
    y.extend(range(1, count + 1))     # xếp chồng theo y

# Vẽ Dotplot
plt.figure(figsize=(8, 4))
plt.plot(x, y, "o", markersize=10, alpha=0.6)
plt.title("Biểu đồ Dotplot: Phân bố điểm số")
plt.xlabel("Điểm số")
plt.ylabel("Tần suất")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.show()
