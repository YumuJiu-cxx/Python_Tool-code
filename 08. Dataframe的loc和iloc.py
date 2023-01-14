import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(16).reshape(4, 4), index=list('abcd'), columns=list('ABCD'))
print(df, '\n')

"""
    提取行数据
"""
print('1:')

# loc
print('loc:')
print(df.loc['a'], '\n')  # 取索引为'a'的行

# iloc
print('iloc:')
print(df.iloc[0], '\n')  # 取第1行的数据

"""
    提取列数据
"""
print('2:')

# loc
print('loc:')
print(df.loc[:, ['A']], '\n')  # 取索引为'A'的列

print(df.loc[:, ['A', 'B']], '\n')  # 取索引为'A'和'B'的列

# iloc
print('iloc:')
print(df.iloc[:, [0]], '\n')  # 取第1列的数据

print(df.iloc[:, [0, 1]], '\n')  # 取第1和2列的数据

"""
    提取指定行、指定列数据
"""
print('3:')

# loc
print('loc:')
print(df.loc[['a', 'c'], ['A', 'B']], '\n')  # 提取index为'a','c', column为'A','B'中的数据

# iloc
print('iloc:')
print(df.iloc[[0, 2], [0, 1]], '\n')  # 提取第1和3行，第1和2列中的数据

"""
    提取所有数据
"""
print('4:')

# loc
print('loc:')
print(df.loc[:, :], '\n')  # 取A,B,C,D列的所有行

# iloc
print('iloc:')
print(df.iloc[:, :], '\n')  # 取第0,1,2,3列的所有行

"""
    利用loc函数，根据某个数据来提取数据所在的行
"""
print('5:')

print(df.loc[df['A'] == 0], '\n')  # 提取条件为: A列中数字为0的行数据

print(df.loc[(df['A'] == 0) & (df['B'] == 1)])  # 符合两个筛选条件的行数据
