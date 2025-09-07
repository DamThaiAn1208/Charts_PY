import matplotlib.pyplot as plt

lbl = ["Apple", "Samsung", "Xiaomi", "Oppo", "Khác"]   # tên nhãn
sizes  = [10, 25, 20, 15, 10]                             # % thị phần
colors = ["gold", "skyblue", "lightcoral", "lightgreen", "violet"]  # màu cho từng phần
explode = (0, 0, 0, 0, 0)  # làm nổi phần "Apple" ra ngoài

plt.pie(sizes, labels=lbl, startangle=90, autopct="%1.1f%%", colors=colors, explode=explode, shadow=True)

plt.title("Biểu đồ Pie - Tỷ lệ thị phần smartphone")
plt.axis("equal")   # đảm bảo hình tròn (nếu bỏ đi có thể bị méo thành elip)
plt.show()
