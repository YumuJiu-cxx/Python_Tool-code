import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 24, 37, 2]

# 最大的3个数的索引
max_num_index_list = map(nums.index, heapq.nlargest(3, nums))
max_num_index_list = list(max_num_index_list)
print("最大的3个数的索引:")
print(max_num_index_list)

# 最大的3个数
max_num = []
for i in max_num_index_list:
    max_num.append(nums[i])
print("最大的3个数:")
print(max_num, '\n')

# 最小的4个数的索引
min_num_index_list = map(nums.index, heapq.nsmallest(4, nums))
min_num_index_list = list(min_num_index_list)
print("最小的4个数的索引:")
print(min_num_index_list)

# 最小的4个数
min_num = []
for i in min_num_index_list:
    min_num.append(nums[i])
print("最小的4个数:")
print(min_num)
