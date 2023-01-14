import os
import random
import re
import shutil

# 1 读取文件列表
image_dir = r'image/'  # 一开始的文件夹
img_name_list = os.listdir(image_dir)
print(img_name_list[:5])

# 2 创建一个目标文件夹
result_dir = r'result/'  # 自动创建存放乱序后文件的文件夹
if not os.path.exists(result_dir):
    os.makedirs(result_dir)
    print(f'创建文件夹{result_dir}成功！')

# 3 创建随机数
random_len = len(img_name_list)
img_index = [i for i in range(random_len)]
random.shuffle(img_index)

# 4 开始转移每个文件
for i, img in enumerate(img_name_list):
    dot_index = img.find('.')
    if dot_index > 0:
        img_name = str(img_index[i]) + img[dot_index:]
        shutil.copyfile(image_dir + img, result_dir + img_name)  # 磁盘不够大要将copyfile要改成move，也就是替换原始文件夹的文件
