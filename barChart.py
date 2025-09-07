import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

data = pd.DataFrame({
    "A": np.random.normal(50, 10, 100),
    "B": np.random.normal(30, 5, 100),
    "C": np.random.randint(10, 100, 100),
    "Category": np.random.choice(["X", "Y", "Z"], 100)
})

cat_counts = data["Category"].value_counts()

plt.bar(cat_counts.index, cat_counts.values, color=["red","green","blue"])
plt.title("Bar Chart - Biểu đồ cột")
plt.xlabel("Danh mục")
plt.ylabel("Số lượng")
plt.show()