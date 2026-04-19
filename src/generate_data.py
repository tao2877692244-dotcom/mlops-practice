import pandas as pd
import numpy as np
import os

# 确保 data/raw 文件夹存在
os.makedirs("data/raw", exist_ok=True)

# 生成数据
np.random.seed(42)
data = np.random.rand(10000, 10)
df = pd.DataFrame(data, columns=[f'feature_{i}' for i in range(10)])

# 保存文件
df.to_csv("data/raw/mock_data.csv", index=False)
print("模拟数据已在 data/raw/mock_data.csv 生成")