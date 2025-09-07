# Biểu đồ Time-Series Graph
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Tạo dữ liệu giả lập: Doanh thu hàng tháng trong 2 năm
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", periods=24, freq="M")
revenue = np.random.randint(80, 150, size=24).cumsum()  # doanh thu tích lũy

# Vẽ biểu đồ Time-Series
plt.figure(figsize=(10, 5))
plt.plot(dates, revenue, marker="o", linestyle="-", color="b")
plt.title("Biểu đồ Time-Series: Doanh thu hàng tháng")
plt.xlabel("Thời gian")
plt.ylabel("Doanh thu (triệu đồng)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
