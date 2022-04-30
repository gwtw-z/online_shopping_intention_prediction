from PySide6.QtWidgets import QFileDialog
from ui.main_PyDracula import *
from ui.ui_main_pages import *
import classifier
import pandas as pd
import numpy as np
import datetime
import os
import seaborn as sns


# git config --global http.sslVerify "false"
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(parent=None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.window_maximized_flag = False
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        self.offset = None

        self.maximize_icon = QIcon()
        self.maximize_icon.addFile(r':/icons/images/icons/icon_maximize.png', QSize(), QIcon.Normal, QIcon.Off)
        self.restore_icon = QIcon()
        self.restore_icon.addFile(r':/icons/images/icons/icon_restore.png', QSize(), QIcon.Normal, QIcon.Off)
        self.ui.radiobutton_default.setChecked(True)

        self.ui.line_file_path_2.setText('(Default)./save')

        self.my_clf = None
        self.my_length = None
        self.file_path = None
        self.save_path = './save'
        self.result = None
        self.chart = None
        self.table_order = 'Visitor ID'

        self.bind()

    def bind(self):
        self.ui.btn_open_file.clicked.connect(self.choose_file)
        self.ui.btn_analyze.clicked.connect(self.show_analysis)
        self.ui.btn_home.clicked.connect(self.home_page)
        self.ui.btn_widgets.clicked.connect(self.widget_page)
        self.ui.btn_chart.clicked.connect(self.chart_page)
        self.ui.btn_save_page.clicked.connect(self.save_page)
        self.ui.radiobutton_default.clicked.connect(self.select_table_order)
        self.ui.radiobutton_probability.clicked.connect(self.select_table_order)
        self.ui.closeAppBtn.clicked.connect(QCoreApplication.instance().quit)
        self.ui.minimizeAppBtn.clicked.connect(self.showMinimized)
        self.ui.maximizeRestoreAppBtn.clicked.connect(self.maximize_page)
        self.ui.titleRightInfo.mouseMoveEvent = self.mouseMoveEvent
        self.ui.btn_save_path.clicked.connect(self.choose_save_path)
        self.ui.btn_save_file.clicked.connect(self.save_output)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = QPoint(event.position().x(), event.position().y())
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + QPoint(event.scenePosition().x(), event.scenePosition().y()) - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

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

    def chart_page(self):
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
        self.my_clf = classifier.GDBT(file_path=self.file_path, feature_num=17)
        self.my_clf.load_model('GDBT')
        self.my_clf.load_reader()
        self.my_length = len(self.my_clf.test_data)
        self.result = pd.DataFrame({
            'Visitor ID': list(range(1, len(self.my_clf.test_data) + 1)),
            # the way Visitor ID is assigned may be improved later
            'Probability': np.delete(self.my_clf.clf.predict_proba(self.my_clf.test_data), 0, axis=1).ravel(),
            'Intention': self.my_clf.clf.predict(self.my_clf.test_data)
        })
        self.result['Intention'] = self.result['Intention'].apply(lambda x: 'Deal!' if x else 'No, thanks.')
        # self.result['Probability'].value_counts().plot.bar(figsize=(16, 8))
        ax = sns.histplot(self.result['Probability'])
        self.chart = ax.get_figure()
        self.chart.savefig('./temp/plt.png')
        self.ui.label.setPixmap(QPixmap('./temp/plt.png'))

    def select_table_order(self):
        btn_name = self.sender().objectName()
        if btn_name == 'radiobutton_default':
            self.table_order = 'Visitor ID'
        if btn_name == 'radiobutton_probability':
            self.table_order = 'Probability'

        if self.file_path is None:
            return
        if self.table_order == 'Probability':
            self.result = self.result.sort_values(by=self.table_order, ascending=False, ignore_index=True)
        if self.table_order == 'Visitor ID':
            self.result = self.result.sort_values(by=self.table_order, ascending=True, ignore_index=True)
        self.show_analysis()

    def show_analysis(self):
        if self.file_path is None:
            return
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(15)
        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem('Visitor ID'))
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem('Probability'))
        self.ui.tableWidget.setItem(0, 2, QTableWidgetItem('Intention'))
        if self.my_length > 15:
            self.ui.tableWidget.setRowCount(self.my_length)
        for i in range(self.my_length):
            item_id = QTableWidgetItem(str(self.result.loc[i, 'Visitor ID']))
            item_prob = QTableWidgetItem(format(self.result.loc[i, 'Probability'], '.1%'))
            item_out = QTableWidgetItem(str(self.result.loc[i, 'Intention']))
            self.ui.tableWidget.setItem(i + 1, 0, item_id)
            self.ui.tableWidget.setItem(i + 1, 1, item_prob)
            self.ui.tableWidget.setItem(i + 1, 2, item_out)

    def choose_save_path(self):
        self.save_path = QFileDialog.getExistingDirectory(self, '选择保存路径', "./")
        self.ui.line_file_path_2.setText(self.save_path)

    def save_output(self):
        if self.result is None:
            self.ui.label_save_answer.setText('No analysis is performed yet!')
        else:
            self.ui.label_save_answer.setText('Analysis result is saved!')
            path = self.save_path + '/' + datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            if not os.path.exists(path):
                os.mkdir(path)
            self.result.to_excel(path + r'/data.xlsx', index=None)
            self.chart.savefig(path + r'/plot.png')


app = QApplication()
window = MainWindow()
window.show()
app.exec()
