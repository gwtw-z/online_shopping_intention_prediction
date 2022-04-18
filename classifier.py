from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression as LR
from sklearn.ensemble import GradientBoostingClassifier
import pickle
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
from sklearn.model_selection import cross_validate
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from imblearn.over_sampling import SVMSMOTE
from imblearn.combine import SMOTETomek
from imblearn.combine import SMOTEENN
from collections import Counter
import seaborn as sns

top5 = ['PageValues', 'Month', 'ExitRates', 'Weekend', 'Informational_Duration']
top10 = ['PageValues', 'Month', 'ExitRates', 'Weekend', 'Informational_Duration', 'Region', 'OperatingSystems',
         'Administrative_Duration', 'VisitorType', 'ProductRelated_Duration']
mRMR_order = ['PageValues', 'Month', 'ExitRates', 'Weekend', 'Informational_Duration', 'Region', 'OperatingSystems',
              'Administrative_Duration', 'VisitorType', 'ProductRelated_Duration', 'SpecialDay', 'Informational',
              'TrafficType', 'Administrative', 'BounceRates', 'Browser', 'ProductRelated']

origin_file_ = r'C:\Users\zty19\Desktop\毕设\major\repo\data\online_shoppers_intention.csv'
file_ = r'C:\Users\zty19\Desktop\毕设\major\repo\data\sample_100.csv'


class Classifier:
    def __init__(self, file_path, clf_name='', feature_num=len(mRMR_order), over_sample=False, generate_sample=False,
                 sample_volume=100):
        self.clf = None
        self.feature_num = feature_num
        self.over_sample = over_sample
        self.generate_sample = generate_sample
        self.sample_volume = sample_volume
        self.file_path = file_path
        self.train_data = None
        self.train_label = None
        self.test_data = None
        self.test_label = None
        self.sample = None
        self.result = None
        self.clf_name = clf_name
        self.train_time = None

    def train_reader(self):
        table = pd.read_csv(self.file_path)
        y = table.iloc[:, -1]
        table = table.drop(columns=['Revenue'])
        if self.generate_sample is True:
            self.sample = table.sample(n=self.sample_volume)
            self.sample.to_csv(r'./data/sample_' + str(self.sample_volume) + '.csv', index=False)
        table = table[mRMR_order[:self.feature_num]]
        x = pd.get_dummies(table)
        mm = MinMaxScaler(feature_range=(0, 1))
        x = mm.fit_transform(x)

        self.train_data, self.test_data, self.train_label, self.test_label = train_test_split(x, y, test_size=0.3,
                                                                                              random_state=3,
                                                                                              stratify=y)
        if self.over_sample is True:
            smote_tomek = SMOTEENN(random_state=3)
            self.train_data, self.train_label = smote_tomek.fit_resample(self.train_data, self.train_label)

        self.train_label = np.array(self.train_label).ravel()
        self.test_label = np.array(self.test_label).ravel()

    def load_reader(self):
        table = pd.read_csv(self.file_path)
        table = table[mRMR_order[:self.feature_num]]
        x = pd.get_dummies(table)
        mm = MinMaxScaler(feature_range=(0, 1))
        x = mm.fit_transform(x)
        self.test_data = x

    def data_sample_generator(self, num=100, output=False, file_name='sample'):
        index = np.random.randint(low=0, high=len(self.test_data), size=num)
        sample = np.concatenate((self.test_data[0].reshape(1, -1), self.test_label[0].reshape(1, -1)), axis=1)
        for i in index:
            line = np.concatenate((self.test_data[i].reshape(1, -1), self.test_label[i].reshape(1, -1)), axis=1)
            sample = np.concatenate((sample, line), axis=0)
        sample = np.delete(sample, 0, axis=0)

        if output is True:
            out = pd.DataFrame(sample)
            out.to_csv(file_name + '.csv')

        return sample

    def train(self):
        start = time.time()
        self.clf.fit(self.train_data, self.train_label.ravel())
        end = time.time()
        self.train_time = end - start
        print(self.clf_name + ':\ntraining time:', self.train_time)

    def score(self):
        self.result = cross_validate(self.clf, self.test_data, self.test_label, cv=10,
                                     scoring=['accuracy', 'f1', 'roc_auc'])

    def show(self):
        print('accuracy:{:.10f}\tf1-score:{:.10f}\tauc:{:.10f}\n'.format(self.result['test_accuracy'].mean(),
                                                                         self.result['test_f1'].mean(),
                                                                         self.result['test_roc_auc'].mean()))

    def save_model(self):
        with open(r'./model/clf.pickle', 'wb') as f:
            pickle.dump(self.clf, f)

    def load_model(self):
        with open(r'./model/clf.pickle', 'rb') as f:
            self.clf = pickle.load(f)

    def start(self):
        self.train()
        self.score()
        self.show()


class NaiveBayes(Classifier):
    def __init__(self, file_path, feature_num=3):
        super(NaiveBayes, self).__init__(file_path, clf_name='naive bayes', feature_num=feature_num)
        self.clf = GaussianNB()


class KNN(Classifier):
    def __init__(self, file_path, n=5, feature_num=3):
        super(KNN, self).__init__(file_path, clf_name='knn', feature_num=feature_num)
        self.clf = KNeighborsClassifier(n_neighbors=n)


class DecisionTree(Classifier):
    def __init__(self, file_path, feature_num=3):
        super(DecisionTree, self).__init__(file_path, clf_name='decision tree', feature_num=feature_num)
        self.clf = tree.DecisionTreeClassifier(criterion='gini')


class RandomForest(Classifier):
    def __init__(self, file_path, n=100, feature_num=12):
        super(RandomForest, self).__init__(file_path, clf_name='random forest', feature_num=feature_num)
        self.clf = RandomForestClassifier(n_estimators=n, random_state=3)


class SVM(Classifier):
    def __init__(self, file_path, c=2, feature_num=3):
        super(SVM, self).__init__(file_path, clf_name='svm', feature_num=feature_num)
        self.clf = svm.SVC(C=c, kernel='rbf')


class MLP(Classifier):
    def __init__(self, file_path, feature_num=3):
        super(MLP, self).__init__(file_path, clf_name='MLP', feature_num=feature_num)
        self.clf = MLPClassifier(solver='adam', alpha=0.5, hidden_layer_sizes=(50, 50, 50, 50, 50),
                                 learning_rate='adaptive', learning_rate_init=0.15, shuffle=True,
                                 max_iter=5000, random_state=1)


class LogisticRegression(Classifier):
    def __init__(self, file_path, feature_num=3):
        super(LogisticRegression, self).__init__(file_path, clf_name='LogisticRegression', feature_num=feature_num)
        self.clf = LR()


class GDBT(Classifier):
    def __init__(self, file_path, n=100, lr=0.5, feature_num=3):
        super(GDBT, self).__init__(file_path, clf_name='GDBT', feature_num=feature_num)
        self.clf = GradientBoostingClassifier(n_estimators=n, learning_rate=lr)


# clf = RandomForest(origin_file_)
# clf.reader()
# clf.train()
# clf.score()
# clf.show()
#
# clf.file_path=(file_)
# clf.reader()
# clf.score()
# clf.show()
# clf = RandomForest(origin_file_)
# clf.start()
# clf.save_model()

# clf = Classifier(origin_file_, generate_sample=True, sample_volume=1000)
# clf.train_reader()
