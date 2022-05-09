from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
# from xgboost.sklearn import XGBClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression as LR
from sklearn.model_selection import GridSearchCV
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

origin_file_ = r'D:\repos\毕设\major\repo\online_shopping_intention_prediction\data\online_shoppers_intention.csv'
file_ = r'D:\repos\毕设\major\repo\online_shopping_intention_prediction\data\sample_10.csv'
new_data = r'D:\repos\毕设\major\repo\online_shopping_intention_prediction\data\breast_cancer.csv'


def normalize(table):
    # 抽样后分类属性可能缺失，与标准表格拼接补全
    column = ['Administrative', 'Administrative_Duration', 'Informational', 'Informational_Duration',
              'ProductRelated', 'ProductRelated_Duration',
              'BounceRates', 'ExitRates', 'PageValues', 'SpecialDay',
              'OperatingSystems', 'Browser', 'Region', 'TrafficType', 'Weekend',
              'Month_Aug', 'Month_Dec', 'Month_Feb', 'Month_Jul', 'Month_June',
              'Month_Mar', 'Month_May', 'Month_Nov', 'Month_Oct', 'Month_Sep',
              'VisitorType_New_Visitor', 'VisitorType_Other',
              'VisitorType_Returning_Visitor']
    df = pd.DataFrame(columns=column, index=[-1])
    return pd.concat([df, table]).drop(index=[-1], axis=1).fillna(0)


class Classifier:
    # 默认读取全部特征，不过采样，不生成样本
    def __init__(self, file_path=origin_file_, clf_name='', feature_num=len(mRMR_order), over_sample=False,
                 generate_sample=False, sample_volume=100):
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
        self.grid_result = None
        self.clf_name = clf_name
        self.train_time = None

    def train_reader(self):
        table = pd.read_csv(self.file_path)
        y = table.iloc[:, -1]
        table = table.iloc[:, :-1]
        if self.generate_sample is True:
            self.sample = table.sample(n=self.sample_volume)
            self.sample.to_csv(r'./data/sample_' + str(self.sample_volume) + '.csv', index=False)
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

    def load_reader(self, is_user_diy_model=False):
        table = pd.read_csv(self.file_path)
        x = pd.get_dummies(table)
        if is_user_diy_model is False:
            x = normalize(x)
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

    def tuning(self, param, scoring):
        grid_search = GridSearchCV(self.clf, param, scoring=scoring, n_jobs=-1, cv=10, refit=False, verbose=2)
        self.grid_result = grid_search.fit(self.test_data, self.test_label)
        # print('best ' + scoring + ':', grid_search.best_score_)
        # print('best parameters:', grid_search.best_params_)

    def train(self, training_time=False):
        start = time.time()
        self.clf.fit(self.train_data, self.train_label.ravel())
        end = time.time()
        self.train_time = end - start
        if training_time is True:
            print(self.clf_name + ':\ntraining time:', self.train_time)

    def score(self):
        self.result = cross_validate(self.clf, self.test_data, self.test_label, cv=10,
                                     scoring=['accuracy', 'f1', 'roc_auc'])

    def show(self):
        print('accuracy:{:.10f}\tauc:{:.10f}\n'.format(self.result['test_accuracy'].mean(),
                                                       self.result['test_roc_auc'].mean()))

    def save_model(self, model):
        with open(model, 'wb') as f:
            pickle.dump(self.clf, f)

    def load_model(self, model):
        with open(model, 'rb') as f:
            self.clf = pickle.load(f)

    def generate_model(self, model_name):
        self.train_reader()
        self.train()
        self.score()
        self.show()
        self.save_model(model_name)


class NaiveBayes(Classifier):
    def __init__(self, file_path, feature_num=17):
        super(NaiveBayes, self).__init__(file_path, clf_name='Naive Bayes', feature_num=feature_num)
        self.clf = GaussianNB()


class KNN(Classifier):
    def __init__(self, file_path, n=25, feature_num=17, over_sample=False):
        # n_neighbors:24  mean_test_accuracy:0.8491467076832929 mean_test_roc_auc:0.7277925234465007
        # n_neighbors:28 mean_test_accuracy:0.8477953563319417  mean_test_roc_auc:0.7317958347476091

        # over_sampled:
        # n_neighbors:9 mean_test_accuracy:0.8526616860763202 mean_test_roc_auc:0.7239525303420712
        # n_neighbors:25 mean_test_accuracy:0.8496879806635904 mean_test_roc_auc:0.7420600929031179
        super(KNN, self).__init__(file_path, clf_name='KNN', feature_num=feature_num, over_sample=over_sample)
        self.clf = KNeighborsClassifier(n_neighbors=n)


class DecisionTree(Classifier):
    def __init__(self, file_path, feature_num=17):
        super(DecisionTree, self).__init__(file_path, clf_name='Decision Tree', feature_num=feature_num)
        self.clf = tree.DecisionTreeClassifier(criterion='gini')


class RandomForest(Classifier):
    def __init__(self, file_path, max_depth=8, n_estimators=68, feature_num=17, over_sample=False):
        # n_estimators:84 max_depth:8 test_accuracy:0.896187 roc_auc:0.914586
        # n_estimators:99 max_depth:8 test_accuracy:0.895104 roc_auc:0.915525

        # over_sampled:
        # n_estimators:51 max_depth:13 test_accuracy:0.895376 roc_auc:0.911067
        # n_estimators:68 max_depth:8 test_accuracy:0.892941 roc_auc:0.915193
        super(RandomForest, self).__init__(file_path, clf_name='Random Forest', feature_num=feature_num,
                                           over_sample=over_sample)
        self.clf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=3)


class SVM(Classifier):
    def __init__(self, file_path, c=5, gamma=0.078125, feature_num=17, over_sample=False):
        # C:49 gamma:0.15625 test_accuracy:0.881857 roc_auc:0.859042
        # C:5 gamma:0.078125 test_accuracy:0.868071 roc_auc:0.876636

        # over_sampled:
        # C:49 gamma:0.15625 test_accuracy:0.881857  roc_auc:0.859042
        # C:5 gamma:0.078125 test_accuracy:0.868071 roc_auc:0.876636
        super(SVM, self).__init__(file_path, clf_name='SVM', feature_num=feature_num, over_sample=over_sample)
        self.clf = svm.SVC(C=c, gamma=gamma, kernel='rbf', probability=True)


class MLP(Classifier):
    def __init__(self, file_path, feature_num=17, over_sample=False):
        super(MLP, self).__init__(file_path, clf_name='MLP', feature_num=feature_num, over_sample=over_sample)
        self.clf = MLPClassifier(solver='sgd', alpha=0.0000, hidden_layer_sizes=(50, 40, 30, 20, 10),
                                 early_stopping=False, learning_rate='constant', learning_rate_init=0.15, shuffle=True,
                                 max_iter=10000)


class LogisticRegression(Classifier):
    def __init__(self, file_path, feature_num=17):
        super(LogisticRegression, self).__init__(file_path, clf_name='LogisticRegression', feature_num=feature_num)
        self.clf = LR()


class GBDT(Classifier):
    def __init__(self, file_path, lr=0.2, n_estimators=18, max_depth=3, feature_num=17, over_sample=False):
        # over_sampled:
        # n_estimators:13 max_depth:3 test_accuracy:0.894294 roc_auc:0.914158
        # n_estimators:18 max_depth:3 test_accuracy:0.892402 roc_auc:0.917063
        super(GBDT, self).__init__(file_path, clf_name='GDBT', feature_num=feature_num, over_sample=over_sample)
        self.clf = GradientBoostingClassifier(n_estimators=n_estimators, max_depth=max_depth, learning_rate=lr)


# class XGBoost(Classifier):
#     def __init__(self, file_path, n=10, lr=0.1, feature_num=17):
#         super(XGBoost, self).__init__(file_path, clf_name='xgboost', feature_num=feature_num)
#         self.clf = XGBClassifier(object='binary:logistic', n_estimators=n, learning_rate=lr, use_label_encoder=False)

# clf = SVM(origin_file_)
# clf.train_reader()
# clf.train()
# clf.score()
# clf.show()
# clf.clf.predict_proba(clf.train_data)

# param = {
#     'n_neighbors': np.arange(2, 30)
# }
# clf = KNN(origin_file_, over_sample=True)
# clf.train_reader()
# clf.tuning(param, ['accuracy', 'roc_auc'])
# result = pd.DataFrame(clf.grid_result.cv_results_)

# clf = GBDT(origin_file_)
# clf.train_reader()
# clf.train()
# clf.score()
# clf.show()
# print(clf.clf.feature_importances_)
