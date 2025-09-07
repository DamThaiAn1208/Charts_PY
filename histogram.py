import numpy as np
import matplotlib.pyplot as plt

# Tạo dữ liệu mẫu: điểm thi 200 học sinh
np.random.seed(42)
scores = np.random.normal(loc=7, scale=1.5, size=200)  # phân phối chuẩn
scores = np.clip(scores, 0, 10)  # giới hạn điểm từ 0 đến 10

# Vẽ Histogram
plt.hist(scores, bins=10, color="skyblue", edgecolor="black")
plt.title("Biểu đồ Histogram - Phân phối điểm thi")
plt.xlabel("Điểm")
plt.ylabel("Số học sinh")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.figure()

# Histogram mật độ
plt.hist(scores, bins=10, density=True, 
         color="lightgreen", edgecolor="black", alpha=0.7)
plt.title("Histogram dạng mật độ")
plt.xlabel("Điểm")
plt.ylabel("Mật độ xác suất")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
