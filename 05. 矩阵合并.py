"""
    罗列了两种矩阵类型的合并方法，分别为numpy和list
    numpy 1.1 最实用
    list 2.1 最实用
"""

"""
    numpy数组
"""
import numpy as np

a = np.array([[1, 3], [5, 7]])
b = np.array([[2, 4], [6, 8]])
c = np.array([[10, 20], [30, 40]])

print("矩阵a及其大小:")
print(a)
print(a.shape, '\n')

print("矩阵b及其大小:")
print(b)
print(b.shape, '\n')

# append()合并
append_1 = np.append(a, b)  # 2个二维矩阵合并成1个一维矩阵
print("矩阵append_1及其大小:")
print(append_1)
print(append_1.shape, '\n')

append_2 = np.append(a, b, axis=0)  # 矩阵竖向合并
print("矩阵append_2及其大小:")
print(append_2)
print(append_2.shape, '\n')

append_3 = np.append(a, b, axis=1)  # 矩阵横向合并
print("矩阵append_3及其大小:")
print(append_3)
print(append_3.shape, '\n')

# stack()合并
# vstack()竖向合并，hstack()横向合并，功能重复已删减
stack_1 = np.stack((a, b))  # 沿新轴连接一系列数组，2个二维矩阵直接合并成1个三维矩阵
print("矩阵stack_1及其大小:")
print(stack_1)
print(stack_1.shape, '\n')

stack_2 = np.dstack((a, b, c))  # 按顺序深度堆叠阵列，2个二维矩阵合并成1个三维矩阵，并且每一位对应的位置合在一起
print("矩阵stack_2及其大小:")
print(stack_2)
print(stack_2.shape, '\n')

"""
    list列表
"""
list_1 = [[1, 3], [5, 7]]
list_2 = [[2, 4], [6, 8]]

print("矩阵list_1及其大小:")
print(list_1)
print(len(list_1), '\n')

print("矩阵list_2及其大小:")
print(list_2)
print(len(list_2), '\n')

# 相加
list_3 = list_1 + list_2
print("矩阵list_3及其大小:")
print(list_3)
print(len(list_3), '\n')

# append()合并
# append会将list_5整个列表并入list_4
# 示例1
list_4 = [[1, 3], [5, 7]]
list_5 = [[2, 4], [6, 8]]

list_4.append(list_5)
print("矩阵list_4及其大小:")
print(list_4)
print(len(list_4), '\n')

# 示例2
list_6 = [[10, 30], [50, 70]]
list_7 = [40, 80]

list_6.append(list_7)
print("矩阵list_6及其大小:")
print(list_6)
print(len(list_6), '\n')

# extend()合并
# extend会将list_9进行拆分一层后，再并入list_8
# 示例1
list_8 = [[1, 3], [5, 7]]
list_9 = [[2, 4], [6, 8]]

list_8.extend(list_9)
print("矩阵list_8及其大小:")
print(list_8)
print(len(list_8), '\n')

# 示例2
list_10 = [[10, 30], [50, 70]]
list_11 = [40, 80]

list_10.extend(list_11)
print("矩阵list_10及其大小:")
print(list_10)
print(len(list_10))
