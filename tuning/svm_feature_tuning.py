from classifier import SVM
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from tqdm import tqdm

accu = []
f1 = []
k_range = range(1, 16, 1)
for i in tqdm(k_range):
    clf = SVM(c=12, feature_num=i)
    clf.train()
    clf.score()
    accu.append(clf.result['test_accuracy'].mean())
    f1.append(clf.result['test_f1'].mean())

plt.figure(figsize=(8, 4), dpi=80)
plt.plot(k_range, accu, color="red", label="accuracy-feature_num curve")
plt.plot(k_range, f1, color="blue", label="f1 score-feature_num curve")
plt.xlabel('feature number')
plt.ylabel('accuracy')

x_major_locator = MultipleLocator(5)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.set_title('relationship between accuracy and number of feature number', fontsize=14)

plt.grid()
plt.legend(loc='best')
plt.show()

best_accu = accu.index(max(accu))
best_f1 = f1.index(max(f1))

print('best accuracy: {} at {}\nbest f1-score: {} at {}'.format(accu[best_accu], best_accu, f1[best_f1], best_f1))
