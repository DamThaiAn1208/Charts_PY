import stemgraphic
import matplotlib.pyplot as plt

# Dữ liệu điểm thi
data = [5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 4, 5, 6, 7, 7, 8, 9]

# Vẽ biểu đồ stem-and-leaf
stemgraphic.stem_graphic(data, scale=10)

plt.show()