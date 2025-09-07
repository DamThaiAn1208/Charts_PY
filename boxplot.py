#Biểu đồ Boxplot (Biểu đồ hộp)
import numpy as np
import matplotlib.pyplot as plt
#----------------------
#Tạo dữ liệu điểm của 3 lớp học
np.random.seed(42)
lop_A = np.random.normal(7, 1.0, 50)    # mean=7, std=1
lop_B = np.random.normal(6, 1.2, 50)    # mean=6, std=1.2
lop_C = np.random.normal(8, 0.8, 50)    # mean=8, std=0.8
data = [lop_A, lop_B, lop_C]
#----------------------
#Vẽ Boxplot
plt.figure(figsize=(7,5))
plt.boxplot(data, labels=["Lớp A", "Lớp B", "Lớp C"], patch_artist=True)
plt.title("Biểu đồ Boxplot: So sánh điểm 3 lớp học")
plt.ylabel("Điểm")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()