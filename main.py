from PySide6.QtWidgets import QFileDialog
from ui.main_PyDracula import *
from ui.ui_main_pages import *
import classifier
import pandas as pd
import numpy as np


# git config --global http.sslVerify "false"

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.window_maximized_flag = False
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.maximize_icon = QIcon()
        self.maximize_icon.addFile(r':/icons/images/icons/icon_maximize.png', QSize(), QIcon.Normal, QIcon.Off)
        self.restore_icon = QIcon()
        self.restore_icon.addFile(r':/icons/images/icons/icon_restore.png', QSize(), QIcon.Normal, QIcon.Off)
        self.ui.radiobutton_default.setChecked(True)

        self.my_clf = None
        self.file_path = None
        self.result = None
        self.table_order = 'Visitor ID'

        self.bind()

    def bind(self):
        self.ui.btn_open_file.clicked.connect(self.choose_file)
        self.ui.btn_analyze.clicked.connect(self.show_analysis)
        self.ui.btn_home.clicked.connect(self.home_page)
        self.ui.btn_widgets.clicked.connect(self.widget_page)
        self.ui.btn_chart.clicked.connect(self.plot_page)
        self.ui.btn_save.clicked.connect(self.save_page)
        self.ui.radiobutton_default.clicked.connect(self.select_table_order)
        self.ui.radiobutton_probability.clicked.connect(self.select_table_order)
        self.ui.closeAppBtn.clicked.connect(QCoreApplication.instance().quit)
        self.ui.minimizeAppBtn.clicked.connect(self.showMinimized)
        self.ui.maximizeRestoreAppBtn.clicked.connect(self.maximize_page)

    def mousePressEvent(self, QMouseEvent):
        # 改为拖动按钮
        if QMouseEvent.button() == Qt.LeftButton:
            self.flag = True
            # 获取鼠标相对窗口的位置
            self.m_Position = QMouseEvent.globalPos() - self.pos()
            QMouseEvent.accept()
        # 更改鼠标图标
        # self.setCursor(QCursor(Qt.OpenHandCursor))

    def maximize_page(self):
        if self.window_maximized_flag is False:
            self.showMaximized()
            self.ui.maximizeRestoreAppBtn.setIcon(self.restore_icon)
            self.ui.maximizeRestoreAppBtn.setToolTip('Restore')
            self.window_maximized_flag = True
        else:
            self.showNormal()
            self.ui.maximizeRestoreAppBtn.setIcon(self.maximize_icon)
            self.ui.maximizeRestoreAppBtn.setToolTip('Maximize')
            self.window_maximized_flag = False

    def home_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

    def widget_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.widgets)

    def plot_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.chart_page)

    def save_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.save_page)

    def choose_file(self):
        self.file_path = QFileDialog.getOpenFileName(
            self,
            '选择数据文件',
            r'.',
            '(*.csv)'
        )[0]
        self.ui.line_file_path.setText(self.file_path)

        # data is processed when file path is chosen instead of when 'analyze' button is pressed
        # so that the user doesn't actually sense the time spent here
        self.my_clf = classifier.RandomForest(file_path=self.file_path)
        self.my_clf.load_model()
        self.my_clf.load_reader()
        self.ui.tableWidget.setRowCount(len(self.my_clf.test_data))
        self.result = pd.DataFrame({
            'Visitor ID': list(range(1, len(self.my_clf.test_data) + 1)),
            'Probability': np.delete(self.my_clf.clf.predict_proba(self.my_clf.test_data), 0, axis=1).ravel(),
            'Intention': self.my_clf.clf.predict(self.my_clf.test_data)
        })
        self.result['Intention'] = self.result['Intention'].apply(lambda x: 'Deal!' if x else 'No, thanks.')

    def select_table_order(self):
        btn_name = self.sender().objectName()
        if btn_name == 'radiobutton_default':
            self.table_order = 'Visitor ID'
        if btn_name == 'radiobutton_probability':
            self.table_order = 'Probability'
        self.show_analysis()

    def show_analysis(self):
        if self.file_path is None:
            return
        # self.my_clf = classifier.RandomForest(file_path=self.file_path)
        # self.my_clf.load_model()
        # self.my_clf.load_reader()
        # self.ui.tableWidget.setRowCount(len(self.my_clf.test_data))
        # self.result = pd.DataFrame({
        #     'Visitor ID': list(range(1, len(self.my_clf.test_data) + 1)),
        #     'Probability': np.delete(self.my_clf.clf.predict_proba(self.my_clf.test_data), 0, axis=1).ravel(),
        #     'Intention': self.my_clf.clf.predict(self.my_clf.test_data)
        # })
        # self.result['Intention'] = self.result['Intention'].apply(lambda x: 'Deal!' if x else 'No, thanks.')
        # print(self.result)
        # self.result[1] = list(map(lambda x: 'Deal!' if x else 'No, thanks.', self.result[1]))
        if self.table_order == 'Probability':
            self.result = self.result.sort_values(by=self.table_order, ascending=False, ignore_index=True)
        if self.table_order == 'Visitor ID':
            self.result = self.result.sort_values(by=self.table_order, ascending=True, ignore_index=True)
        # data = zip(self.result[0], self.result[1])
        # for i, (prob, out) in enumerate(data, start=1):
        #     item_id = QTableWidgetItem(str(i))
        #     # item_prob = QTableWidgetItem(str(round(Decimal(prob[1]), 3)))
        #     item_prob = QTableWidgetItem(format(prob[1], '.1%'))
        #     item_out = QTableWidgetItem(str(out))
        #     self.ui.tableWidget.setItem(i, 0, item_id)
        #     self.ui.tableWidget.setItem(i, 1, item_prob)
        #     self.ui.tableWidget.setItem(i, 2, item_out)
        for i in range(len(self.result)):
            item_id = QTableWidgetItem(str(self.result.loc[i, 'Visitor ID']))
            item_prob = QTableWidgetItem(format(self.result.loc[i, 'Probability'], '.1%'))
            item_out = QTableWidgetItem(str(self.result.loc[i, 'Intention']))
            self.ui.tableWidget.setItem(i + 1, 0, item_id)
            self.ui.tableWidget.setItem(i + 1, 1, item_prob)
            self.ui.tableWidget.setItem(i + 1, 2, item_out)


app = QApplication()
window = MainWindow()
window.show()
app.exec()
