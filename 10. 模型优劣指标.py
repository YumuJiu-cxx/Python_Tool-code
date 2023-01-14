"""
    FP: 实际为负，但被预测为正的样本数量
    TN: 实际为负，也预测为负的样本数量
    TP: 实际为正，也预测为正的样本数量
    FN: 实际为正，但被预测为负的样本数量
"""

import numpy as np
from sklearn.metrics import accuracy_score

"""
    准确率
    Accuracy = TP + TN / TP + TN + FP + FN
"""
y_pred = [0, 2, 1, 3]
y_true = [0, 1, 2, 3]
print("准确率:")
print(accuracy_score(y_true, y_pred))  # 0.5
print(accuracy_score(y_true, y_pred, normalize=False))  # 2 (返回分类正确的样本数量)

# 在具有二元标签指示符的多标签分类案例中
print(accuracy_score(np.array([[0, 1], [1, 1]]), np.ones((2, 2))), '\n')  # 0.5

"""
    精确率
    Precision = TP / TP + FP
"""
from sklearn.metrics import precision_score

y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 2, 1, 0, 0, 1]
print("精确率:")
print(precision_score(y_true, y_pred, average='macro'))  # 0.2222222222222222
print(precision_score(y_true, y_pred, average='micro'))  # 0.3333333333333333
print(precision_score(y_true, y_pred, average='weighted'))  # 0.2222222222222222
print(precision_score(y_true, y_pred, average=None), '\n')  # [0.66666667 0. 0.]

"""
    召回率
    Recall = TP / TP + FN
"""
from sklearn.metrics import recall_score

y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 2, 1, 0, 0, 1]
print("召回率:")
print(recall_score(y_true, y_pred, average='macro'))  # 0.3333333333333333
print(recall_score(y_true, y_pred, average='micro'))  # 0.3333333333333333
print(recall_score(y_true, y_pred, average='weighted'))  # 0.3333333333333333
print(recall_score(y_true, y_pred, average=None), '\n')  # [1. 0. 0.]

"""
    F1 score
    F1 = 2 * precision * recall / precision + recall
"""
from sklearn.metrics import f1_score

y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 2, 1, 0, 0, 1]
print("F1分数:")
print(f1_score(y_true, y_pred, average='macro'))  # 0.26666666666666666
print(f1_score(y_true, y_pred, average='micro'))  # 0.3333333333333333
print(f1_score(y_true, y_pred, average='weighted'))  # 0.26666666666666666
print(f1_score(y_true, y_pred, average=None))  # [0.8 0. 0.]
