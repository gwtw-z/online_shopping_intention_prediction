from mpl_toolkits.mplot3d import Axes3D
from classifier import RandomForest, GDBT, SVM, origin_file_
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# x_means = 'n_estimators'
# x = np.arange(10, 50)
# y_means = 'max_depth'
# y = np.arange(3, 20)

x_means = 'C'
x = np.arange(5, 50)
y_means = 'gamma'
y = [1 / 0.1, 1 / 0.2, 1 / 0.4, 1 / 0.6, 1 / 0.8, 1 / 1.6, 1 / 3.2, 1 / 6.4, 1 / 12.8]

para = {
    x_means: x,
    y_means: y
}

clf = SVM(origin_file_)
clf.train_reader()
clf.tuning(para, ['accuracy', 'roc_auc'])
result = pd.DataFrame(clf.grid_result.cv_results_)

Z1 = np.array(result['mean_test_accuracy']).reshape(len(y), len(x))
Z2 = np.array(result['mean_test_roc_auc']).reshape(len(y), len(x))
X, Y = np.meshgrid(x, y)

fig = plt.figure('gird search')
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z1, cmap=plt.cm.rainbow)
# ax.plot_surface(X, Y, Z2, cmap=plt.cm.rainbow)
ax.view_init(40, -30)
ax.set_xlabel(x_means)
ax.set_ylabel(y_means)
ax.set_zlabel('accuracy')
plt.show(block=True)

print(result[result['rank_test_accuracy'] == 1][
          ['param_' + x_means, 'param_' + y_means, 'mean_test_accuracy', 'mean_test_roc_auc']])

print(result[result['rank_test_roc_auc'] == 1][
          ['param_' + x_means, 'param_' + y_means, 'mean_test_accuracy', 'mean_test_roc_auc']])

# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# import numpy as np
#
# def himmelbau(x):
#     return (x[0]**2 + x[1] - 1)**2 + (x[0] + x[1] **2 -7)**2
#
# x = np.arange(-6,6,0.1)
# y = np.arange(-6,6,0.1)
# print('x,y range:',x.shape,y.shape)
# X,Y = np.meshgrid(x,y)
# Z = himmelbau([X,Y])
# #绘制himmelblau 函数曲面
# fig = plt.figure('himmelblau')
# ax = fig.gca(projection='3d')
# ax.plot_surface(X,Y,Z,cmap=plt.cm.rainbow)
# ax.view_init(60,-30)
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# plt.show()
