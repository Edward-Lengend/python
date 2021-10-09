counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'LEGION': 199, 'acer': 99}

# 需求：提取上述电脑数量>=200的字典数量
count = {key:value for key, value in counts.items() if value >= 200}
print(count)