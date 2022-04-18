# empty

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#
#         self.file_path = None
#         self.my_clf = None
#         self.result = None
#         self.sub = None
#
#         self.bind()
#
#     def bind(self):
#         self.ui.button_choose_file.clicked.connect(self.choose_file)
#         self.ui.button_start.clicked.connect(self.start)
#
#     def choose_file(self):
#         self.file_path = QFileDialog.getOpenFileName(
#             self,
#             '选择数据文件',
#             r'.',
#             '(*.csv)'
#         )[0]
#         self.ui.label_file_path.setText(self.file_path)
#
#     def start(self):
#         self.my_clf = classifier.RandomForest(file_path=self.file_path)
#         self.my_clf.load_model()
#         self.my_clf.reader()
#         self.result = [
#             self.my_clf.clf.predict_proba(self.my_clf.test_data),
#             self.my_clf.clf.predict(self.my_clf.test_data)
#         ]
#         print(self.result)
#         self.sub = TableWindow(self.result)
#         self.sub.show()
#
#
# class TableWindow(QWidget):
#     def __init__(self, data, parent=None):
#         super(TableWindow, self).__init__(parent)
#         self.setWindowTitle('分析结果')
#
#         self.table = QTableWidget()
#         self.table.setRowCount(len(data[0]))
#         self.table.setColumnCount(2)
#         self.table.setHorizontalHeaderLabels(['预测概率', '预测结果'])
#
#         data = zip(data[0], data[1])
#         for i, (prob, out) in enumerate(data):
#             item_prob = QTableWidgetItem(str(round(prob[1], 10)))
#             item_out = QTableWidgetItem(str(out))
#             self.table.setItem(i, 0, item_prob)
#             self.table.setItem(i, 1, item_out)
#
#         layout = QVBoxLayout(self)
#         layout.addWidget(self.table)