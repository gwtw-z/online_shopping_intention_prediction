import numpy
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
from sklearn.metrics import roc_auc_score
from imblearn.combine import SMOTETomek
from classifier import Classifier
from collections import Counter
import seaborn as sns
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

myNet = nn.Sequential(
    nn.Linear(28, 50),
    nn.ReLU(),
    nn.Linear(50, 40),
    nn.ReLU(),
    nn.Linear(40, 30),
    nn.ReLU(),
    nn.Linear(30, 20),
    nn.ReLU(),
    nn.Linear(20, 1),
)

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(DEVICE)
myNet = myNet.to(DEVICE)


def test(predict, label):
    predict = numpy.array(predict)
    label = numpy.array(label)
    t = predict == label
    accu = np.mean(t)
    return accu


table = pd.read_csv('./data/online_shoppers_intention.csv')
table = shuffle(table, random_state=3)
y = table.iloc[:, -1].apply(lambda x: 1 if x is True else 0)
table = table.drop(columns=['Revenue'])
X = pd.get_dummies(table)
mm = MinMaxScaler(feature_range=(0, 1))
X = mm.fit_transform(X)
train_data, test_data, train_label, test_label = train_test_split(X, y, test_size=0.3, random_state=3, stratify=y)
test_label = np.array(test_label).ravel()
train_label = np.array(train_label).ravel()

# smote_tomek = SMOTETomek(random_state=3)
# train_data, train_label = smote_tomek.fit_resample(train_data, train_label)
# print('over-sampling done\n')

# myNet = Net()
criterion = nn.MSELoss()  # 损失函数
optimizer = torch.optim.SGD(myNet.parameters(), lr=0.15)  # 优化器
epochs = 5000  # 训练次数
accuracy = []
roc_auc = []


def check(cur_epoch):
    with torch.no_grad():
        test_in = torch.from_numpy(test_data).float().to(DEVICE)
        test_out = myNet(test_in).squeeze().cpu()
        for i in range(len(test_out)):
            if test_out[i] < 0.5:
                test_out[i] = 0
            else:
                test_out[i] = 1
        if cur_epoch % 50 == 0:
            accu = test(test_label, test_out)
            f1 = f1_score(test_label, test_out)
            auc = roc_auc_score(test_label, test_out)
            accuracy.append(accu)
            roc_auc.append(auc)
            if cur_epoch % 500 == 0:
                print(
                    "Epoch:{}\tLoss:{:.10f}\tAccuracy:{:.10f}\tf1-score:{:.10f}\tauc:{:.10f}".format(cur_epoch,
                                                                                                     loss.item(),
                                                                                                     accu, f1, auc))


for i in range(epochs):
    x_ = torch.from_numpy(train_data).float().to(DEVICE)
    y_ = torch.from_numpy(train_label).float().to(DEVICE)
    out = myNet(x_).squeeze()
    loss = criterion(out, y_)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    # if i % 500 == 0:  # 每100次输出相关的信息
    #     check(i)
    check(i)

check(epochs)
data = pd.DataFrame({'accu': accuracy, 'auc': roc_auc})
plt.plot(data[['accu', 'auc']])
plt.xlabel('epoch(×50)')
plt.title('accuracy and roc_auc in training epochs')
plt.legend(['accuracy', 'roc_auc'], loc='best')
plt.show(block=True)
