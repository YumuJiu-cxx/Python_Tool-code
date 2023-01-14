import pandas as pd

a = [[1, 9, 2], [1, 8, 5], [9, 9, 9]]
df = pd.DataFrame(a)
print(df, '\n')

print('第1列各数字重复的次数: ')
print(df[0].value_counts(), '\n')  # 查看第1列各项数量

print('第2列各数字重复的次数: ')
print(df[1].value_counts(), '\n')  # 查看第2列各项数量

print('第3列各数字重复的次数: ')
print(df[2].value_counts())  # 查看第3列各项数量
