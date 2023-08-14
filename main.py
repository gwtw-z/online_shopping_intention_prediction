from PySide6.QtWidgets import QFileDialog
from ui.main_PyDracula import *
from ui.ui_main_pages import *
from settings import Settings
import classifier
import pandas as pd
import numpy as np
import datetime
import os
import shutil
import seaborn as sns


# git config --global http.sslVerify "false"
# os.environ["QT_FONT_DPI"] = "96"


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(parent=None)
        self.group = None
        self.right_box = None
        self.left_box = None
        self.animation = None
        self.offset = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.window_maximized_flag = False
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.ui.btn_home_page.setStyleSheet(self.selectMenu(self.ui.btn_home_page.styleSheet()))
        self.ui.label_home_picture.setPixmap(QPixmap(r'./images/images/PyPredict.png'))
        self.current_btn = self.ui.btn_home_page

        self.maximize_icon = QIcon()
        self.maximize_icon.addFile(r':/icons/images/icons/icon_maximize.png', QSize(), QIcon.Normal, QIcon.Off)
        self.restore_icon = QIcon()
        self.restore_icon.addFile(r':/icons/images/icons/icon_restore.png', QSize(), QIcon.Normal, QIcon.Off)
        self.ui.radiobutton_default.setChecked(True)
        self.ui.line_save_file_path.setText('(Default)./save')
        self.ui.leftMenuBg.setMinimumWidth(Settings.MENU_WIDTH)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.model_path = './model/GBDT.pickle'  # default model
        self.current_model = '(Default)GBDT'
        self.my_clf = None
        self.my_length = None
        self.file_path = None
        self.save_path = './save'
        self.result = None
        self.chart = None
        self.table_order = 'Visitor ID'
        self.new_data = None
        self.user_diy_clf = None
        self.new_model_path = './model'
        self.is_diy_model = False

        self.bind()

    def bind(self):
        self.ui.btn_open_file.clicked.connect(self.select_file)
        self.ui.btn_analyze.clicked.connect(self.show_analysis)
        self.ui.btn_home_page.clicked.connect(self.widget_page)
        self.ui.btn_analyze_page.clicked.connect(self.widget_page)
        self.ui.btn_chart_page.clicked.connect(self.widget_page)
        self.ui.btn_save_page.clicked.connect(self.widget_page)
        self.ui.radiobutton_default.clicked.connect(self.select_table_order)
        self.ui.radiobutton_probability.clicked.connect(self.select_table_order)
        self.ui.closeAppBtn.clicked.connect(QCoreApplication.instance().quit)
        self.ui.minimizeAppBtn.clicked.connect(self.showMinimized)
        self.ui.maximizeRestoreAppBtn.clicked.connect(self.maximize_page)
        self.ui.titleRightInfo.mouseMoveEvent = self.mouseMoveEvent
        self.ui.btn_save_path.clicked.connect(self.choose_save_path)
        self.ui.btn_save_file.clicked.connect(self.save_output)
        self.ui.toggleButton.clicked.connect(self.toggleMenu)
        self.ui.toggleLeftBox.clicked.connect(self.toggleLeftBox)
        self.ui.extraCloseColumnBtn.clicked.connect(self.toggleLeftBox)
        self.ui.btn_adjust_page.clicked.connect(self.widget_page)
        self.ui.btn_diy_page.clicked.connect(self.widget_page)
        self.ui.btn_select_model.clicked.connect(self.select_model)
        self.ui.btn_select_new_data.clicked.connect(self.select_new_data)
        self.ui.btn_train_new_model.clicked.connect(self.train_new_model)
        self.ui.btn_select_path_new_model.clicked.connect(self.select_path_save_new_model)
        self.ui.btn_save_new_model.clicked.connect(self.save_new_model)

    # SELECT
    def selectMenu(self, get_style):
        select = get_style + Settings.MENU_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectMenu(self, get_style):
        deselect = get_style.replace(Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

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

    # def home_page(self):
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
    #     self.current_btn.setStyleSheet(self.deselectMenu(self.current_btn.styleSheet()))
    #     self.current_btn = self.ui.btn_home_page
    #     self.current_btn.setStyleSheet(self.selectMenu(self.current_btn.styleSheet()))
    #
    # def analyze_page(self):
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.analyze_page)
    #     self.current_btn.setStyleSheet(self.deselectMenu(self.current_btn.styleSheet()))
    #     self.current_btn = self.ui.btn_analyze_page
    #     self.current_btn.setStyleSheet(self.selectMenu(self.current_btn.styleSheet()))
    #
    # def chart_page(self):
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.chart_page)
    #     self.current_btn.setStyleSheet(self.deselectMenu(self.current_btn.styleSheet()))
    #     self.current_btn = self.ui.btn_chart_page
    #     self.current_btn.setStyleSheet(self.selectMenu(self.current_btn.styleSheet()))
    #
    # def save_page(self):
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.save_page)
    #     self.current_btn.setStyleSheet(self.deselectMenu(self.current_btn.styleSheet()))
    #     self.current_btn = self.ui.btn_save_page
    #     self.current_btn.setStyleSheet(self.selectMenu(self.current_btn.styleSheet()))
    #
    # def adjust_page(self):
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.adjust_page)
    #
    # def diy_page(self):
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.diy_page)

    def widget_page(self):
        self.current_btn.setStyleSheet(self.deselectMenu(self.current_btn.styleSheet()))
        self.current_btn = self.sender()
        self.current_btn.setStyleSheet(self.selectMenu(self.current_btn.styleSheet()))
        if self.current_btn.objectName() == 'btn_home_page':
            self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        if self.current_btn.objectName() == 'btn_analyze_page':
            self.ui.stackedWidget.setCurrentWidget(self.ui.analyze_page)
        if self.current_btn.objectName() == 'btn_chart_page':
            self.ui.stackedWidget.setCurrentWidget(self.ui.chart_page)
        if self.current_btn.objectName() == 'btn_save_page':
            self.ui.stackedWidget.setCurrentWidget(self.ui.save_page)
        if self.current_btn.objectName() == 'btn_adjust_page':
            self.ui.stackedWidget.setCurrentWidget(self.ui.adjust_page)
        if self.current_btn.objectName() == 'btn_diy_page':
            self.ui.stackedWidget.setCurrentWidget(self.ui.diy_page)

    def pick_model_name(self):
        return self.model_path.split('/')[-1].split('.')[0]

    def select_model(self):
        model_path = QFileDialog.getOpenFileName(
            self,
            '选择分析模型',
            r'./model',
            '(*.pickle)'
        )[0]
        if model_path == '':
            return
        self.model_path = model_path
        self.ui.line_model_path.setText(self.model_path)
        self.current_model = self.pick_model_name()
        self.ui.label_model.setText('The current model selected is : ' + self.current_model)

    def select_file(self):
        file_path = QFileDialog.getOpenFileName(
            self,
            '选择数据文件',
            r'./data',
            '(*.csv)'
        )[0]
        if file_path == '':
            return
        self.file_path = file_path
        self.ui.line_file_path.setText(self.file_path)
        self.calculate()

    def calculate(self):
        # data is processed when file path is chosen instead of when 'analyze' button is pressed
        # so that the user doesn't actually sense the time spent here
        if self.file_path is None or self.model_path is None:
            return
        self.my_clf = classifier.Classifier(file_path=self.file_path, feature_num=17)
        self.is_diy_model = False
        if self.pick_model_name()[:3] == 'DIY':
            self.is_diy_model = True
        self.my_clf.load_model(self.model_path)
        self.my_clf.load_reader(is_user_diy_model=self.is_diy_model)
        self.my_length = len(self.my_clf.test_data)
        self.result = pd.DataFrame({
            'Visitor ID': list(range(1, self.my_length + 1)),
            # the way Visitor ID is assigned may be improved later
            'Probability': np.delete(self.my_clf.clf.predict_proba(self.my_clf.test_data), 0, axis=1).ravel(),
            'Intention': self.my_clf.clf.predict(self.my_clf.test_data)
        })
        if self.is_diy_model is False:
            self.result['Intention'] = self.result['Intention'].apply(lambda x: 'Deal!' if x else 'No, thanks.')
        else:
            self.result['Intention'] = self.result['Intention'].apply(lambda x: 'True' if x else 'False')
        sns.set(style='dark')
        ax = sns.histplot(self.result['Probability'], kde=True, bins=min(20, self.my_length))
        self.chart = ax.get_figure()
        if not os.path.exists('./temp'):
            os.mkdir('./temp')
        self.chart.savefig('./temp/plt.png')
        self.ui.label.setPixmap(QPixmap('./temp/plt.png'))
        ax.clear()  # ax not cleared, there would be trouble analyzing more data

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
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(15)
        if self.my_length > 15:
            self.ui.tableWidget.setRowCount(self.my_length)
        for i in range(self.my_length):
            item_id = QTableWidgetItem(str(self.result.loc[i, 'Visitor ID']))
            item_prob = QTableWidgetItem(format(self.result.loc[i, 'Probability'], '.1%'))
            item_out = QTableWidgetItem(str(self.result.loc[i, 'Intention']))
            item_id.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item_prob.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item_out.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            self.ui.tableWidget.setItem(i, 0, item_id)
            self.ui.tableWidget.setItem(i, 1, item_prob)
            self.ui.tableWidget.setItem(i, 2, item_out)

    def choose_save_path(self):
        save_path = QFileDialog.getExistingDirectory(
            self,
            '选择保存路径',
            './save'
        )
        if save_path == '':
            return
        else:
            self.save_path = save_path
            self.ui.line_save_file_path.setText(save_path)

    def save_output(self):
        if self.result is None:
            self.ui.label_save_answer.setText('No analysis is done yet!')
        else:
            self.ui.label_save_answer.setText('Analysis result is saved!')
            path = self.save_path + '/' + datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            if not os.path.exists(path):
                os.mkdir(path)
            self.result.to_excel(path + r'/data.xlsx', index=None)
            # self.chart.savefig(path + r'/chart.png') # this does not work
            shutil.copy(r'./temp/plt.png', path)

    def select_new_data(self):
        new_data = QFileDialog.getOpenFileName(
            self,
            '选择数据文件',
            r'./data',
            '(*.csv)'
        )[0]
        if new_data == '':
            return
        self.new_data = new_data
        self.ui.line_file_path_new_data.setText(new_data)

    def train_new_model(self):
        model_name = self.ui.model_choice.currentText()
        if model_name == '(choose a model)':
            return
        if model_name == 'KNN':
            self.user_diy_clf = classifier.KNN(self.new_data)
        if model_name == 'Decision Tree':
            self.user_diy_clf = classifier.DecisionTree(self.new_data)
        if model_name == 'Random Forest':
            self.user_diy_clf = classifier.RandomForest(self.new_data)
        if model_name == 'GBDT':
            self.user_diy_clf = classifier.GBDT(self.new_data)
        self.user_diy_clf.train_reader()
        self.user_diy_clf.train(training_time=False)
        score = classifier.cross_validate(self.user_diy_clf.clf, self.user_diy_clf.test_data,
                                          self.user_diy_clf.test_label, cv=10, scoring=['accuracy'])
        self.ui.label_train_result.setText(
            'Training result:  ' + model_name + ' got ' + str(format(score['test_accuracy'].mean(), '.2%'))
            + ' accuracy in ' + str(format(self.user_diy_clf.train_time, '.5f')) + 's')

    def select_path_save_new_model(self):
        save_path = QFileDialog.getExistingDirectory(
            self,
            '选择保存路径',
            r'./model'
        )
        if save_path == '':
            return
        self.new_model_path = save_path
        self.ui.line_file_path_new_model.setText(save_path)

    def save_new_model(self):
        self.user_diy_clf.save_model(self.new_model_path + '/DIY_' + self.user_diy_clf.clf_name + '.pickle')
        self.ui.label_diy_model_info.setText('DIY model is save!')

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0

        # Check values
        if left_box_width == 0 and direction == 'left':
            left_width = 240
        else:
            left_width = 0
        # Check values
        if right_box_width == 0 and direction == 'right':
            right_width = 240
        else:
            right_width = 0

            # ANIMATION LEFT BOX
        self.left_box = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX
        self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")
        self.right_box.setDuration(Settings.TIME_ANIMATION)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup(parent=None)
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    def toggleMenu(self):
        # GET WIDTH
        width = self.ui.leftMenuBg.width()
        maxExtend = Settings.MENU_WIDTH
        standard = 60

        # SET MAX WIDTH
        if width == 60:
            widthExtended = maxExtend
        else:
            widthExtended = standard

        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
        self.animation.setDuration(Settings.TIME_ANIMATION)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def toggleLeftBox(self):
        # GET WIDTH
        width = self.ui.extraLeftBox.width()
        widthRightBox = self.ui.extraRightBox.width()
        maxExtend = Settings.LEFT_BOX_WIDTH
        color = Settings.BTN_LEFT_BOX_COLOR
        standard = 0

        # GET BTN STYLE
        style = self.ui.toggleLeftBox.styleSheet()

        # SET MAX WIDTH
        if width == 0:
            widthExtended = maxExtend
            # SELECT BTN
            self.ui.toggleLeftBox.setStyleSheet(style + color)
            # if widthRightBox != 0:
            #     style = self.ui.settingsTopBtn.styleSheet()
            #     self.ui.settingsTopBtn.setStyleSheet(style.replace(Settings.BTN_RIGHT_BOX_COLOR, ''))
        else:
            widthExtended = standard
            # RESET BTN
            self.ui.toggleLeftBox.setStyleSheet(style.replace(color, ''))

        self.start_box_animation(width, widthRightBox, 'left')


app = QApplication()
window = MainWindow()
window.show()
app.exec()
