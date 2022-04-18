from PySide6.QtWidgets import QFileDialog
from ui.main_PyDracula import *
from ui.ui_main_pages import *
import classifier


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
        # self.ui.btn_home.setToolTip('home')
        # self.ui.btn_analyze.setToolTip('analyze')
        # self.ui.btn_chart.setToolTip('chart')
        # self.ui.btn_save.setToolTip('save')

        self.file_path = None
        self.my_clf = None
        self.result = None

        self.bind()

    def bind(self):
        self.ui.btn_open_file.clicked.connect(self.choose_file)
        self.ui.btn_analysize.clicked.connect(self.analyze)
        self.ui.btn_home.clicked.connect(self.home_page)
        self.ui.btn_widgets.clicked.connect(self.widget_page)
        self.ui.btn_chart.clicked.connect(self.plot_page)
        self.ui.closeAppBtn.clicked.connect(QCoreApplication.instance().quit)
        self.ui.minimizeAppBtn.clicked.connect(self.showMinimized)
        self.ui.maximizeRestoreAppBtn.clicked.connect(self.maximize_page)
        # test

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

    def choose_file(self):
        self.file_path = QFileDialog.getOpenFileName(
            self,
            '选择数据文件',
            r'.',
            '(*.csv)'
        )[0]
        self.ui.line_file_path.setText(self.file_path)

    def analyze(self):
        self.my_clf = classifier.RandomForest(file_path=self.file_path)
        self.my_clf.load_model()
        self.my_clf.load_reader()
        self.result = [
            self.my_clf.clf.predict_proba(self.my_clf.test_data),
            self.my_clf.clf.predict(self.my_clf.test_data)
        ]
        # print(self.result)
        self.ui.tableWidget.setRowCount(len(self.result[0]))
        self.result[1] = list(map(lambda x: 'Deal!' if x else 'No, thanks.', self.result[1]))
        data = zip(self.result[0], self.result[1])
        for i, (prob, out) in enumerate(data, start=1):
            item_id = QTableWidgetItem(str(i))
            item_prob = QTableWidgetItem(str(round(prob[1], 10)))
            item_out = QTableWidgetItem(str(out))
            self.ui.tableWidget.setItem(i, 0, item_id)
            self.ui.tableWidget.setItem(i, 1, item_prob)
            self.ui.tableWidget.setItem(i, 2, item_out)


app = QApplication()
window = MainWindow()
window.show()
app.exec()
