import numpy as np
import matplotlib.pyplot as plt

#----------------------
#Tạo dữ liệu mẫu: Chiều cao (cm) và Cân nặng (kg) của 100 người
np.random.seed(42)
height = np.random.normal(165, 10, 100)   # chiều cao ~ N(165, 10)
weight = 0.4 * height + np.random.normal(20, 5, 100)
#cân nặng có tương quan với chiều cao

#----------------------
#Vẽ Scatterplot
plt.figure(figsize=(7,5))
plt.scatter(height, weight, color="blue", alpha=0.6, edgecolor="k")
plt.title("Biểu đồ Scatterplot: Chiều cao vs Cân nặng")
plt.xlabel("Chiều cao (cm)")
plt.ylabel("Cân nặng (kg)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()