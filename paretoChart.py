import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Tạo dữ liệu mẫu: Lỗi sản xuất và
data = {
    "Nguyên nhân": ["Sai kích thước","Nứt bề mặt", "Màu sai", "Lỗi hàn","Khuyết tật vật liệu"],
    "Số lỗi": [45, 30, 15, 7, 3]
    }
df = pd.DataFrame(data)

# Sắp xếp giảm dần theo số lỗi
df = df.sort_values(by="Số lỗi", ascending=False).reset_index(drop=True)

# Tính % tích lũy
df["Phần trăm"] = 100 * df["Số lỗi"] / df["Số lỗi"].sum()
df["% tích lũy"] = df["Phần trăm"].cumsum()

# -----------------------------
# Vẽ biểu đồ Pareto
fig, ax1 = plt.subplots()

# Biểu đồ cột (số lỗi)
ax1.bar(df["Nguyên nhân"], df["Số lỗi"], color="C0")
ax1.set_xlabel("Nguyên nhân")
ax1.set_ylabel("Số lỗi", color="C0")
#ax1.tick_params(axis="y", labelcolor="C0")

# Trục y thứ 2 để vẽ đường tích lũy %
ax2 = ax1.twinx()
ax2.plot(df["Nguyên nhân"], df["% tích lũy"], color="C1", marker="x", linewidth=2)
ax2.set_ylabel("% tích lũy",color="C1")
#ax2.tick_params(axis="y",labelcolor="C1")
ax2.axhline(80 , color="r", linestyle="--")

# Vạch 80% (quy tắc Pareto)
# Tiêu đề
plt.title("Biểu đồ Pareto - Phân tích nguyên nhân lỗi")
plt.show()