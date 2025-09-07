def stem_and_leaf_plot(data):
    data = sorted(data)  # sắp xếp dữ liệu
    stem_dict = {}
    for num in data:
        stem, leaf = divmod(num, 10)  # tách nhánh và lá
        stem_dict.setdefault(stem, []).append(leaf)

    for stem, leaves in stem_dict.items():
        print(f"{stem} | {' '.join(map(str, leaves))}")

# Ví dụ
data = [12, 15, 17, 22, 23, 25, 27, 32, 34, 35, 41]
stem_and_leaf_plot(data)

