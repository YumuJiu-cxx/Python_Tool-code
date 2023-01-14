import numpy as np

'''将list转化为numpy.ndarray'''

# 定义一个list
list = [1, 2, 3, 4, 5, 6]
# 输出list和它的类型
print(list)
print(type(list))

# 将list转化为numpy.ndarray
array = np.array(list)
print(array)
print(type(array), '\n')

'''将numpy.ndarray转化为list'''

# 定义一个numpy.ndarray
array = np.array([1, 2, 3, 4, 5, 6])
# 输出numpy.ndarray和它的类型
print(array)
print(type(array))

# 将numpy.ndarray转化为list
list = array.tolist()
print(list)
print(type(list))
