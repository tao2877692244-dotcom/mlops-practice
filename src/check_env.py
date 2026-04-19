import sys
import pandas as pd

print("--- 环境检查报告 ---")
# sys.executable 会告诉你当前用的 Python 是哪个位置的
print(f"当前 Python 引擎位置: {sys.executable}")
print(f"Pandas 版本: {pd.__version__}")
print("--- 检查完毕，环境配置正确 ---")