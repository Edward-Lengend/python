import matplotlib.pyplot as plt
import numpy as np
stock_change = np.random.uniform(0, 2, (8, 10))
# print(stock_change) # 里面的数是浮点数

new_stock = stock_change.astype(np.int32)
print(new_stock)