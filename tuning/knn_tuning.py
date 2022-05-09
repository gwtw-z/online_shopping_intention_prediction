from classifier import KNN, origin_file_
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from tqdm import tqdm
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate

accu = []
f1 = []
auc = []
k_range = range(1, 30)
for i in tqdm(k_range):
    clf = KNN(origin_file_, n=i + 1, over_sample=False)
    clf.train_reader()
    # clf.train()
    # clf.score()
    scores_accu = cross_val_score(clf.clf, clf.test_data, clf.test_label.ravel(), scoring='accuracy', cv=10)
    scores_auc = cross_val_score(clf.clf, clf.test_data, clf.test_label.ravel(), scoring='roc_auc', cv=10)
    # accu.append(clf.result['test_accuracy'].mean())
    # f1.append(clf.result['test_f1'].mean())
    # auc.append(clf.result['test_roc_auc'].mean())
    accu.append(scores_accu.mean())
    auc.append(scores_auc.mean())

plt.rcParams['font.size'] = 14
plt.figure(figsize=(12, 6), dpi=140)
plt.plot(k_range, accu, color="red", label="accuracy")
plt.plot(k_range, auc, color="blue", label="auc")
plt.xlabel('n_neighbors')
# plt.ylabel('accuracy/auc')

x_major_locator = MultipleLocator(1)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
# ax.set_title('relationship between accuracy and number of n_neighbors', fontsize=14)

plt.grid()
plt.legend(loc='best')
# plt.savefig(r'../grid_search/fixed_over_sample/KNN.png', bbox_inches='tight', pad_inches=0)
plt.show(block=True)

f1.append(0)
best_accu = accu.index(max(accu))
best_f1 = f1.index(max(f1))
best_auc = auc.index(max(auc))

print('best accuracy: {} at {}\nbest f1-score: {} at {}\nbest auc: {} at {}'.format(accu[best_accu], best_accu,
                                                                                    f1[best_f1], best_f1, auc[best_auc],
                                                                                    best_auc))
