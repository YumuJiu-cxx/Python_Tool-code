import numpy as np

a = [[3, 1], [0, 1], [5, 2], [8, 6]]
a = np.array(a)
print("矩阵a及其大小:")
print(a)
print(a.shape, '\n')

b = [[4, 1, 5], [2, 2, 8]]
b = np.array(b)
print("矩阵b及其大小:")
print(b)
print(b.shape, '\n')

c = np.dot(a, b)
# [[3×4+1×2 3×1+1×2 3×5+1×8]
#  [0×4+1×2 0×1+1×2 0×5+1×8]
#  [5×4+2×2 5×1+2×2 5×5+2×8]
#  [8×4+6×2 8×1+6×2 8×5+6×8]]
print("矩阵c=a×b:")
print(c)
print(c.shape, '\n')

d = [[1], [2], [3], [4]]
d = np.array(d)
print("矩阵d及其大小:")
print(d)
print(d.shape, '\n')

e = c + d
print("矩阵e=c+d:")
print(e)
print(e.shape)
