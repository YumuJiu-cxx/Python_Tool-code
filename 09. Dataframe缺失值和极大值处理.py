import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(6, 3), columns=['col_1', 'col_2', 'col_3'])
df.iloc[1:2, [1, 2]] = np.nan  # 2和3行的第2列为空值
df.iloc[4:6, 0] = np.inf  # 5和6行的第1列为无穷大值
print(df, '\n')

print('查看空值:')
print(df[(df.isnull()).any(1)], '\n')
print('查看无穷大值:')
print(df[(np.isinf(df)).any(1)], '\n')

"""
    无穷值处理
"""
df.replace(np.inf, 0, inplace=True)  # 把无穷大改为0
print('消除Inf:')
print(df, '\n')

"""
    空值处理
"""
# 删除空值整行
df_2 = df.dropna()
print("直接删除空值:")
print(df_2, '\n')

# 临界值填补
df_3 = df.fillna(method="ffill")  # 把NaN上面的值赋予空值
df_4 = df.fillna(method="bfill")  # 把NaN下面的值赋予空值
print("用NaN上面的值填补空值:")
print(df_3, '\n')
print("用NaN下面的值填补空值:")
print(df_4, '\n')

# 均值填补
df_5 = df.fillna(df.mean()['col_1':'col_3'])
print("用均值填补空值:")
print(df_5, '\n')

# 指定值填充
df_6 = df.fillna({'col_1': 10, 'col_2': 20, 'col_3': 30})
print("用指定值填补空值:")
print(df_6)
