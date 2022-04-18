from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn import svm
from sklearn import datasets
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import pandas as pd
import numpy as np
import time
from tqdm import trange
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.model_selection import cross_val_score
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from imblearn.over_sampling import SVMSMOTE
from imblearn.combine import SMOTETomek
from imblearn.combine import SMOTEENN
from collections import Counter

top5 = ['PageValues', 'Month', 'ExitRates', 'Weekend', 'Informational_Duration']
top10 = ['PageValues', 'Month', 'ExitRates', 'Weekend', 'Informational_Duration', 'Region', 'OperatingSystems',
         'Administrative_Duration', 'VisitorType', 'ProductRelated_Duration']

file = r'C:\Users\zty19\Desktop\毕设\major\repo\online_shoppers_intention.csv'

table = pd.read_csv(file)
y = table.iloc[:, -1]
table = table.drop(columns=['Revenue'])
# table = table[top5]
x = pd.get_dummies(table)
mm = MinMaxScaler(feature_range=(0, 1))
x = mm.fit_transform(x)

train_data, test_data, train_label, test_label = train_test_split(x, y, test_size=0.3, random_state=3,
                                                                  stratify=y)
smote_tomek = SMOTETomek(random_state=3)
train_data, train_label = smote_tomek.fit_resample(train_data, train_label)
test_label = np.array(test_label).ravel()
train_label = np.array(train_label).ravel()

clf = GaussianNB()
clf.fit(train_data, train_label.ravel())
accu = cross_val_score(clf, test_data, test_label, cv=10).mean()
predict = clf.predict(test_data)
f1 = f1_score(test_label, predict)

print('\naccuracy:{:.10f}\tf1-score:{:.10f}\n'.format(accu, f1))
