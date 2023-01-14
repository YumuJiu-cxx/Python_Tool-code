"""np.meshgrid 使用范例"""

import numpy as np

nx, ny = (3, 6)
print("nx：")
print(nx, '\n')
print("ny：")
print(ny, '\n')

x = np.linspace(0, 1, nx)  # 把0~1分成3份，3份中包括0和1
y = np.linspace(0, 1, ny)  # 把0~1分成6份，6份中包括0和1
print("x：")
print(x, '\n')
print("y：")
print(y, '\n')

# 从坐标向量返回坐标矩阵
xv, yv = np.meshgrid(x, y)  # 创建shape=(6, 3)的二维矩阵
print("xv：")
print(xv, '\n')
print("yv：")
print(yv)
