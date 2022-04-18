import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim
from torch.nn.init import kaiming_normal_
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from imblearn.combine import SMOTETomek
from classifier import Classifier
from collections import Counter
import seaborn as sns
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

myNet = nn.Sequential(
    nn.Linear(28, 50),
    nn.ReLU(),
    nn.Linear(50, 50),
    nn.ReLU(),
    nn.Linear(50, 50),
    nn.ReLU(),
    nn.Linear(50, 50),
    nn.ReLU(),
    nn.Linear(50, 1),
)


def test(predict, label):
    t = predict == label
    accu = np.mean(t)
    return accu


table = pd.read_csv('online_shoppers_intention.csv')
table = shuffle(table, random_state=3)
y = table.iloc[:, -1].apply(lambda x: 1 if x is True else 0)
table = table.drop(columns=['Revenue'])
X = pd.get_dummies(table)
# scatter_matrix(X, s=32, alpha=1, c=y, figsize=(25, 25))  # 散点矩阵图
# plt.suptitle("music data divided into 2 centroids", fontsize=50)
mm = MinMaxScaler(feature_range=(0, 1))
X = mm.fit_transform(X)
train_data, test_data, train_label, test_label = train_test_split(X, y, test_size=0.3, random_state=3, stratify=y)
test_label = np.array(test_label).ravel()
train_label = np.array(train_label).ravel()

smote_tomek = SMOTETomek(random_state=3)
train_data, train_label = smote_tomek.fit_resample(train_data, train_label)
print('over-sampling done\n')

# myNet = Net()
criterion = nn.MSELoss()  # 损失函数
optimizer = torch.optim.SGD(myNet.parameters(), lr=0.15)  # 优化器
epochs = 10000  # 训练次数


def check(epoch):
    with torch.no_grad():
        test_in = torch.from_numpy(test_data).float()
        test_out = myNet(test_in).squeeze().numpy()
        for i in range(len(test_out)):
            if test_out[i] < 0.5:
                test_out[i] = 0
            else:
                test_out[i] = 1
        accu = test(test_out, test_label)
        f1 = f1_score(test_label, test_out)
        print("Epoch:{}\tLoss:{:.10f}\tAccuracy:{:.10f}\tF1-score:{:.10f}".format(epoch, loss.item(), accu, f1))


for i in range(epochs):
    x_ = torch.from_numpy(train_data).float()
    y_ = torch.from_numpy(train_label).float()
    out = myNet(x_).squeeze()
    loss = criterion(out, y_)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if i % 500 == 0:  # 每100次输出相关的信息
        check(i)
check(epochs)
