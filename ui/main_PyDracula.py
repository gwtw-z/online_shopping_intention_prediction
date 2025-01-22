# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_PyDracula.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1277, 787)
        MainWindow.setMinimumSize(QSize(940, 560))
        icon = QIcon()
        icon.addFile(u"images/images/PyDracula.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.styleSheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home_page = QPushButton(self.topMenu)
        self.btn_home_page.setObjectName(u"btn_home_page")
        sizePolicy.setHeightForWidth(self.btn_home_page.sizePolicy().hasHeightForWidth())
        self.btn_home_page.setSizePolicy(sizePolicy)
        self.btn_home_page.setMinimumSize(QSize(0, 45))
        self.btn_home_page.setFont(font)
        self.btn_home_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home_page.setLayoutDirection(Qt.LeftToRight)
        self.btn_home_page.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home_page)

        self.btn_analyze_page = QPushButton(self.topMenu)
        self.btn_analyze_page.setObjectName(u"btn_analyze_page")
        sizePolicy.setHeightForWidth(self.btn_analyze_page.sizePolicy().hasHeightForWidth())
        self.btn_analyze_page.setSizePolicy(sizePolicy)
        self.btn_analyze_page.setMinimumSize(QSize(0, 45))
        self.btn_analyze_page.setFont(font)
        self.btn_analyze_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_analyze_page.setLayoutDirection(Qt.LeftToRight)
        self.btn_analyze_page.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-browser.png);\n"
"")

        self.verticalLayout_8.addWidget(self.btn_analyze_page)

        self.btn_chart_page = QPushButton(self.topMenu)
        self.btn_chart_page.setObjectName(u"btn_chart_page")
        sizePolicy.setHeightForWidth(self.btn_chart_page.sizePolicy().hasHeightForWidth())
        self.btn_chart_page.setSizePolicy(sizePolicy)
        self.btn_chart_page.setMinimumSize(QSize(0, 45))
        self.btn_chart_page.setFont(font)
        self.btn_chart_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_chart_page.setLayoutDirection(Qt.LeftToRight)
        self.btn_chart_page.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart-pie.png);")

        self.verticalLayout_8.addWidget(self.btn_chart_page)

        self.btn_save_page = QPushButton(self.topMenu)
        self.btn_save_page.setObjectName(u"btn_save_page")
        sizePolicy.setHeightForWidth(self.btn_save_page.sizePolicy().hasHeightForWidth())
        self.btn_save_page.setSizePolicy(sizePolicy)
        self.btn_save_page.setMinimumSize(QSize(0, 45))
        self.btn_save_page.setFont(font)
        self.btn_save_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_page.setLayoutDirection(Qt.LeftToRight)
        self.btn_save_page.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png);")

        self.verticalLayout_8.addWidget(self.btn_save_page)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setToolTipDuration(-4)
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon1)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_adjust_page = QPushButton(self.extraTopMenu)
        self.btn_adjust_page.setObjectName(u"btn_adjust_page")
        sizePolicy.setHeightForWidth(self.btn_adjust_page.sizePolicy().hasHeightForWidth())
        self.btn_adjust_page.setSizePolicy(sizePolicy)
        self.btn_adjust_page.setMinimumSize(QSize(0, 45))
        self.btn_adjust_page.setFont(font)
        self.btn_adjust_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjust_page.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjust_page.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjust_page)

        self.btn_diy_page = QPushButton(self.extraTopMenu)
        self.btn_diy_page.setObjectName(u"btn_diy_page")
        sizePolicy.setHeightForWidth(self.btn_diy_page.sizePolicy().hasHeightForWidth())
        self.btn_diy_page.setSizePolicy(sizePolicy)
        self.btn_diy_page.setMinimumSize(QSize(0, 45))
        self.btn_diy_page.setFont(font)
        self.btn_diy_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_diy_page.setLayoutDirection(Qt.LeftToRight)
        self.btn_diy_page.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_diy_page)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)

        self.extraTopMenu.raise_()
        self.extraBottom.raise_()
        self.extraCenter.raise_()

        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon1)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"")
        self.verticalLayout_37 = QVBoxLayout(self.home_page)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_home_picture = QLabel(self.home_page)
        self.label_home_picture.setObjectName(u"label_home_picture")
        self.label_home_picture.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_home_picture)

        self.stackedWidget.addWidget(self.home_page)
        self.analyze_page = QWidget()
        self.analyze_page.setObjectName(u"analyze_page")
        self.analyze_page.setStyleSheet(u"b")
        self.verticalLayout_27 = QVBoxLayout(self.analyze_page)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.row_1 = QFrame(self.analyze_page)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.labelVersion_3)

        self.line_file_path = QLineEdit(self.frame_content_wid_1)
        self.line_file_path.setObjectName(u"line_file_path")
        self.line_file_path.setMinimumSize(QSize(0, 30))
        self.line_file_path.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_6.addWidget(self.line_file_path)

        self.btn_open_file = QPushButton(self.frame_content_wid_1)
        self.btn_open_file.setObjectName(u"btn_open_file")
        self.btn_open_file.setMinimumSize(QSize(150, 30))
        self.btn_open_file.setFont(font)
        self.btn_open_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open_file.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open_file.setIcon(icon4)

        self.horizontalLayout_6.addWidget(self.btn_open_file)

        self.btn_analyze = QPushButton(self.frame_content_wid_1)
        self.btn_analyze.setObjectName(u"btn_analyze")
        self.btn_analyze.setMinimumSize(QSize(150, 30))
        self.btn_analyze.setFont(font)
        self.btn_analyze.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_analyze.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-caret-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_analyze.setIcon(icon5)

        self.horizontalLayout_6.addWidget(self.btn_analyze)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout_27.addWidget(self.row_1)

        self.row_3 = QFrame(self.analyze_page)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.row_3)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.radiobutton_default = QRadioButton(self.row_3)
        self.radiobutton_default.setObjectName(u"radiobutton_default")

        self.horizontalLayout_8.addWidget(self.radiobutton_default)

        self.radiobutton_probability = QRadioButton(self.row_3)
        self.radiobutton_probability.setObjectName(u"radiobutton_probability")

        self.horizontalLayout_8.addWidget(self.radiobutton_probability)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)


        self.verticalLayout_28.addLayout(self.horizontalLayout_8)

        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 15):
            self.tableWidget.setRowCount(15)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem20)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(290)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_28.addWidget(self.tableWidget)


        self.verticalLayout_27.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.analyze_page)
        self.chart_page = QWidget()
        self.chart_page.setObjectName(u"chart_page")
        self.verticalLayout_22 = QVBoxLayout(self.chart_page)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.row_2 = QFrame(self.chart_page)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_2 = QFrame(self.row_2)
        self.frame_div_content_2.setObjectName(u"frame_div_content_2")
        self.frame_div_content_2.setMinimumSize(QSize(0, 110))
        self.frame_div_content_2.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_2.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_div_content_2)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_2 = QFrame(self.frame_div_content_2)
        self.frame_title_wid_2.setObjectName(u"frame_title_wid_2")
        self.frame_title_wid_2.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_2.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_title_wid_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.labelBoxBlenderInstalation_2 = QLabel(self.frame_title_wid_2)
        self.labelBoxBlenderInstalation_2.setObjectName(u"labelBoxBlenderInstalation_2")
        self.labelBoxBlenderInstalation_2.setFont(font)
        self.labelBoxBlenderInstalation_2.setStyleSheet(u"")

        self.verticalLayout_21.addWidget(self.labelBoxBlenderInstalation_2)


        self.verticalLayout_20.addWidget(self.frame_title_wid_2)

        self.frame_content_wid_2 = QFrame(self.frame_div_content_2)
        self.frame_content_wid_2.setObjectName(u"frame_content_wid_2")
        self.frame_content_wid_2.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_content_wid_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.labelVersion_4 = QLabel(self.frame_content_wid_2)
        self.labelVersion_4.setObjectName(u"labelVersion_4")
        self.labelVersion_4.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_4.setLineWidth(1)
        self.labelVersion_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.labelVersion_4)

        self.comboBox = QComboBox(self.frame_content_wid_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_7.addWidget(self.comboBox)

        self.comboBox_3 = QComboBox(self.frame_content_wid_2)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_7.addWidget(self.comboBox_3)

        self.labelVersion_5 = QLabel(self.frame_content_wid_2)
        self.labelVersion_5.setObjectName(u"labelVersion_5")
        self.labelVersion_5.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_5.setLineWidth(1)
        self.labelVersion_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.labelVersion_5)

        self.comboBox_2 = QComboBox(self.frame_content_wid_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_7.addWidget(self.comboBox_2)

        self.btn_analysize_2 = QPushButton(self.frame_content_wid_2)
        self.btn_analysize_2.setObjectName(u"btn_analysize_2")
        self.btn_analysize_2.setMinimumSize(QSize(150, 30))
        self.btn_analysize_2.setFont(font)
        self.btn_analysize_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_analysize_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_analysize_2.setIcon(icon6)

        self.horizontalLayout_7.addWidget(self.btn_analysize_2)

        self.btn_analysize_3 = QPushButton(self.frame_content_wid_2)
        self.btn_analysize_3.setObjectName(u"btn_analysize_3")
        self.btn_analysize_3.setMinimumSize(QSize(150, 30))
        self.btn_analysize_3.setFont(font)
        self.btn_analysize_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_analysize_3.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_analysize_3.setIcon(icon7)

        self.horizontalLayout_7.addWidget(self.btn_analysize_3)


        self.verticalLayout_20.addWidget(self.frame_content_wid_2)


        self.verticalLayout_19.addWidget(self.frame_div_content_2)

        self.label = QLabel(self.row_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label)


        self.verticalLayout_22.addWidget(self.row_2)

        self.stackedWidget.addWidget(self.chart_page)
        self.adjust_page = QWidget()
        self.adjust_page.setObjectName(u"adjust_page")
        self.verticalLayout_35 = QVBoxLayout(self.adjust_page)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.row_6 = QFrame(self.adjust_page)
        self.row_6.setObjectName(u"row_6")
        self.row_6.setFrameShape(QFrame.StyledPanel)
        self.row_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.row_6)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_5 = QFrame(self.row_6)
        self.frame_div_content_5.setObjectName(u"frame_div_content_5")
        self.frame_div_content_5.setMinimumSize(QSize(0, 110))
        self.frame_div_content_5.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_5.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_div_content_5)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_5 = QFrame(self.frame_div_content_5)
        self.frame_title_wid_5.setObjectName(u"frame_title_wid_5")
        self.frame_title_wid_5.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_5.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_title_wid_5)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.labelBoxBlenderInstalation_6 = QLabel(self.frame_title_wid_5)
        self.labelBoxBlenderInstalation_6.setObjectName(u"labelBoxBlenderInstalation_6")
        self.labelBoxBlenderInstalation_6.setFont(font)
        self.labelBoxBlenderInstalation_6.setStyleSheet(u"")

        self.verticalLayout_34.addWidget(self.labelBoxBlenderInstalation_6)


        self.verticalLayout_33.addWidget(self.frame_title_wid_5)

        self.frame_content_wid_5 = QFrame(self.frame_div_content_5)
        self.frame_content_wid_5.setObjectName(u"frame_content_wid_5")
        self.frame_content_wid_5.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_content_wid_5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_save_path_4 = QLabel(self.frame_content_wid_5)
        self.label_save_path_4.setObjectName(u"label_save_path_4")
        self.label_save_path_4.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_save_path_4.setLineWidth(1)
        self.label_save_path_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_save_path_4)

        self.line_model_path = QLineEdit(self.frame_content_wid_5)
        self.line_model_path.setObjectName(u"line_model_path")
        self.line_model_path.setMinimumSize(QSize(0, 30))
        self.line_model_path.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.line_model_path)

        self.btn_select_model = QPushButton(self.frame_content_wid_5)
        self.btn_select_model.setObjectName(u"btn_select_model")
        self.btn_select_model.setMinimumSize(QSize(150, 30))
        self.btn_select_model.setFont(font)
        self.btn_select_model.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_select_model.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_select_model.setIcon(icon4)

        self.horizontalLayout_11.addWidget(self.btn_select_model)


        self.verticalLayout_33.addWidget(self.frame_content_wid_5)


        self.verticalLayout_32.addWidget(self.frame_div_content_5)


        self.verticalLayout_35.addWidget(self.row_6)

        self.label_model = QLabel(self.adjust_page)
        self.label_model.setObjectName(u"label_model")
        self.label_model.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_model)

        self.verticalSpacer_3 = QSpacerItem(20, 526, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.adjust_page)
        self.diy_page = QWidget()
        self.diy_page.setObjectName(u"diy_page")
        self.verticalLayout_31 = QVBoxLayout(self.diy_page)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.row_5 = QFrame(self.diy_page)
        self.row_5.setObjectName(u"row_5")
        self.row_5.setFrameShape(QFrame.StyledPanel)
        self.row_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.row_5)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_3 = QFrame(self.row_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_12.addWidget(self.label_2)


        self.verticalLayout_15.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_save_path_6 = QLabel(self.frame_5)
        self.label_save_path_6.setObjectName(u"label_save_path_6")
        self.label_save_path_6.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_save_path_6.setLineWidth(1)
        self.label_save_path_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_save_path_6)

        self.line_file_path_new_data = QLineEdit(self.frame_5)
        self.line_file_path_new_data.setObjectName(u"line_file_path_new_data")
        self.line_file_path_new_data.setMinimumSize(QSize(0, 30))
        self.line_file_path_new_data.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_13.addWidget(self.line_file_path_new_data)

        self.btn_select_new_data = QPushButton(self.frame_5)
        self.btn_select_new_data.setObjectName(u"btn_select_new_data")
        self.btn_select_new_data.setMinimumSize(QSize(150, 30))
        self.btn_select_new_data.setFont(font)
        self.btn_select_new_data.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_select_new_data.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_select_new_data.setIcon(icon4)

        self.horizontalLayout_13.addWidget(self.btn_select_new_data)


        self.verticalLayout_15.addWidget(self.frame_5)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_save_path_5 = QLabel(self.frame)
        self.label_save_path_5.setObjectName(u"label_save_path_5")
        self.label_save_path_5.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_save_path_5.setLineWidth(1)
        self.label_save_path_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_save_path_5)

        self.model_choice = QComboBox(self.frame)
        self.model_choice.addItem("")
        self.model_choice.addItem("")
        self.model_choice.addItem("")
        self.model_choice.addItem("")
        self.model_choice.addItem("")
        self.model_choice.setObjectName(u"model_choice")
        self.model_choice.setCurrentText(u"(choose a model)")

        self.horizontalLayout_10.addWidget(self.model_choice)

        self.btn_train_new_model = QPushButton(self.frame)
        self.btn_train_new_model.setObjectName(u"btn_train_new_model")
        self.btn_train_new_model.setMinimumSize(QSize(150, 30))
        self.btn_train_new_model.setFont(font)
        self.btn_train_new_model.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_train_new_model.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_train_new_model.setIcon(icon5)

        self.horizontalLayout_10.addWidget(self.btn_train_new_model)


        self.verticalLayout_15.addWidget(self.frame)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_train_result = QLabel(self.frame_6)
        self.label_train_result.setObjectName(u"label_train_result")
        self.label_train_result.setFont(font)
        self.label_train_result.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.label_train_result)


        self.verticalLayout_15.addWidget(self.frame_6)


        self.verticalLayout_30.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.row_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_content_wid_7 = QFrame(self.frame_2)
        self.frame_content_wid_7.setObjectName(u"frame_content_wid_7")
        self.frame_content_wid_7.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_content_wid_7)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_save_path_7 = QLabel(self.frame_content_wid_7)
        self.label_save_path_7.setObjectName(u"label_save_path_7")
        self.label_save_path_7.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_save_path_7.setLineWidth(1)
        self.label_save_path_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_save_path_7)

        self.line_file_path_new_model = QLineEdit(self.frame_content_wid_7)
        self.line_file_path_new_model.setObjectName(u"line_file_path_new_model")
        self.line_file_path_new_model.setMinimumSize(QSize(0, 30))
        self.line_file_path_new_model.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_14.addWidget(self.line_file_path_new_model)

        self.btn_select_path_new_model = QPushButton(self.frame_content_wid_7)
        self.btn_select_path_new_model.setObjectName(u"btn_select_path_new_model")
        self.btn_select_path_new_model.setMinimumSize(QSize(150, 30))
        self.btn_select_path_new_model.setFont(font)
        self.btn_select_path_new_model.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_select_path_new_model.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_select_path_new_model.setIcon(icon4)

        self.horizontalLayout_14.addWidget(self.btn_select_path_new_model)

        self.btn_save_new_model = QPushButton(self.frame_content_wid_7)
        self.btn_save_new_model.setObjectName(u"btn_save_new_model")
        self.btn_save_new_model.setMinimumSize(QSize(150, 30))
        self.btn_save_new_model.setFont(font)
        self.btn_save_new_model.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_new_model.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save_new_model.setIcon(icon8)

        self.horizontalLayout_14.addWidget(self.btn_save_new_model)


        self.verticalLayout_29.addWidget(self.frame_content_wid_7)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_diy_model_info = QLabel(self.frame_7)
        self.label_diy_model_info.setObjectName(u"label_diy_model_info")

        self.horizontalLayout_15.addWidget(self.label_diy_model_info)


        self.verticalLayout_29.addWidget(self.frame_7)


        self.verticalLayout_30.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 294, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_2)


        self.verticalLayout_31.addWidget(self.row_5)

        self.stackedWidget.addWidget(self.diy_page)
        self.save_page = QWidget()
        self.save_page.setObjectName(u"save_page")
        self.verticalLayout_26 = QVBoxLayout(self.save_page)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.row_4 = QFrame(self.save_page)
        self.row_4.setObjectName(u"row_4")
        self.row_4.setFrameShape(QFrame.StyledPanel)
        self.row_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.row_4)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_3 = QFrame(self.row_4)
        self.frame_div_content_3.setObjectName(u"frame_div_content_3")
        self.frame_div_content_3.setMinimumSize(QSize(0, 110))
        self.frame_div_content_3.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_3.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_div_content_3)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_3 = QFrame(self.frame_div_content_3)
        self.frame_title_wid_3.setObjectName(u"frame_title_wid_3")
        self.frame_title_wid_3.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_3.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_title_wid_3)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.labelBoxBlenderInstalation_3 = QLabel(self.frame_title_wid_3)
        self.labelBoxBlenderInstalation_3.setObjectName(u"labelBoxBlenderInstalation_3")
        self.labelBoxBlenderInstalation_3.setFont(font)
        self.labelBoxBlenderInstalation_3.setStyleSheet(u"")

        self.verticalLayout_25.addWidget(self.labelBoxBlenderInstalation_3)


        self.verticalLayout_24.addWidget(self.frame_title_wid_3)

        self.frame_content_wid_3 = QFrame(self.frame_div_content_3)
        self.frame_content_wid_3.setObjectName(u"frame_content_wid_3")
        self.frame_content_wid_3.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_save_path = QLabel(self.frame_content_wid_3)
        self.label_save_path.setObjectName(u"label_save_path")
        self.label_save_path.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_save_path.setLineWidth(1)
        self.label_save_path.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_save_path)

        self.line_save_file_path = QLineEdit(self.frame_content_wid_3)
        self.line_save_file_path.setObjectName(u"line_save_file_path")
        self.line_save_file_path.setMinimumSize(QSize(0, 30))
        self.line_save_file_path.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_9.addWidget(self.line_save_file_path)

        self.btn_save_path = QPushButton(self.frame_content_wid_3)
        self.btn_save_path.setObjectName(u"btn_save_path")
        self.btn_save_path.setMinimumSize(QSize(150, 30))
        self.btn_save_path.setFont(font)
        self.btn_save_path.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_path.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_save_path.setIcon(icon4)

        self.horizontalLayout_9.addWidget(self.btn_save_path)

        self.btn_save_file = QPushButton(self.frame_content_wid_3)
        self.btn_save_file.setObjectName(u"btn_save_file")
        self.btn_save_file.setMinimumSize(QSize(150, 30))
        self.btn_save_file.setFont(font)
        self.btn_save_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_file.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_save_file.setIcon(icon8)

        self.horizontalLayout_9.addWidget(self.btn_save_file)


        self.verticalLayout_24.addWidget(self.frame_content_wid_3)


        self.verticalLayout_23.addWidget(self.frame_div_content_3)


        self.verticalLayout_26.addWidget(self.row_4)

        self.label_save_answer = QLabel(self.save_page)
        self.label_save_answer.setObjectName(u"label_save_answer")
        self.label_save_answer.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_save_answer)

        self.verticalSpacer = QSpacerItem(20, 471, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.save_page)

        self.verticalLayout_36.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Prediction System", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyPredict", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Ease your e-commerce", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
#if QT_CONFIG(tooltip)
        self.btn_home_page.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_home_page.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.btn_analyze_page.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_analyze_page.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
#if QT_CONFIG(tooltip)
        self.btn_chart_page.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_chart_page.setText(QCoreApplication.translate("MainWindow", u"Chart", None))
#if QT_CONFIG(tooltip)
        self.btn_save_page.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_save_page.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_adjust_page.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_diy_page.setText(QCoreApplication.translate("MainWindow", u"DIY Workshop", None))
        self.textEdit.setMarkdown(QCoreApplication.translate("MainWindow", u"**PyPredict**\n"
"\n"
"PyPredict is an intelligent system committed to easing your e-commerce, created\n"
"using Pyside6 and color style based on the Dracula theme by Zeno Rocha.\n"
"\n"
"MIT License\n"
"\n"
"System constructed by Homo\n"
"\n"
"UI style contributed by Wanderson M. Pimenta\n"
"\n"
"**Run System**\n"
"\n"
"python main.py\n"
"\n"
"**Redesign GUI**\n"
"\n"
"Pyside6-uic main_PyDracula.ui -o main_PyDracula.py\n"
"\n"
"", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Microsoft YaHei UI'; font-size:9pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyPredict</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px;"
                        " margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">PyPredict is an intelligent system committed to easing your e-commerce, created using Pyside6 and color style based on the Dracula theme by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">System constructed by Homo</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><sp"
                        "an style=\" color:#bd93f9;\">UI style contributed by Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#bd93f9;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Run System</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">python main.py</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; "
                        "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Redesign GUI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">Pyside6-uic main_PyDracula.ui -o main_PyDracula.py</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; color:#ffffff;\"><br /></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Online Shopping Intention Predicting System</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_home_picture.setText("")
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"Please select the data file(*.csv) to analyze.", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Data file path:", None))
        self.line_file_path.setText("")
        self.line_file_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.btn_open_file.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
        self.btn_analyze.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.radiobutton_default.setText(QCoreApplication.translate("MainWindow", u"Default Order", None))
        self.radiobutton_probability.setText(QCoreApplication.translate("MainWindow", u"Sort by Probability ", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Visitor ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Probability", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Intention", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.labelBoxBlenderInstalation_2.setText(QCoreApplication.translate("MainWindow", u"Please select the way to create a pivot chart.", None))
        self.labelVersion_4.setText(QCoreApplication.translate("MainWindow", u"View two attributes:  ", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"month", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"visitor type", None))

#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"month", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"visitor type", None))

#if QT_CONFIG(tooltip)
        self.comboBox_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.labelVersion_5.setText(QCoreApplication.translate("MainWindow", u" in the form of: ", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"bar", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"pie", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Scatter", None))

        self.btn_analysize_2.setText(QCoreApplication.translate("MainWindow", u"Go!", None))
        self.btn_analysize_3.setText(QCoreApplication.translate("MainWindow", u"Hold", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"No pivot chart is created yet.", None))
        self.labelBoxBlenderInstalation_6.setText(QCoreApplication.translate("MainWindow", u"The default model performed best in our test, while the others(*.pickle) are optional here.", None))
        self.label_save_path_4.setText(QCoreApplication.translate("MainWindow", u"Select model path:", None))
        self.line_model_path.setText(QCoreApplication.translate("MainWindow", u"(Default)./model/GBDT.pickle", None))
        self.line_model_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.btn_select_model.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_model.setText(QCoreApplication.translate("MainWindow", u"The current model selected is : (Default) GBDT", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Meet with another problem? Don't worry, because DIY is supported.", None))
        self.label_save_path_6.setText(QCoreApplication.translate("MainWindow", u"Select the path of new problem data : ", None))
        self.line_file_path_new_data.setText("")
        self.line_file_path_new_data.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.btn_select_new_data.setText(QCoreApplication.translate("MainWindow", u"Select path", None))
        self.label_save_path_5.setText(QCoreApplication.translate("MainWindow", u"Select the machine learning model you'd like to use in this problem : ", None))
        self.model_choice.setItemText(0, QCoreApplication.translate("MainWindow", u"(choose a model)", None))
        self.model_choice.setItemText(1, QCoreApplication.translate("MainWindow", u"KNN", None))
        self.model_choice.setItemText(2, QCoreApplication.translate("MainWindow", u"Decision Tree", None))
        self.model_choice.setItemText(3, QCoreApplication.translate("MainWindow", u"Random Forest", None))
        self.model_choice.setItemText(4, QCoreApplication.translate("MainWindow", u"GBDT", None))

        self.btn_train_new_model.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.label_train_result.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">  Training result:</span></p></body></html>", None))
        self.label_save_path_7.setText(QCoreApplication.translate("MainWindow", u"Select the path to save your new model : ", None))
        self.line_file_path_new_model.setText(QCoreApplication.translate("MainWindow", u"(Default)./model", None))
        self.line_file_path_new_model.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.btn_select_path_new_model.setText(QCoreApplication.translate("MainWindow", u"Select path", None))
        self.btn_save_new_model.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_diy_model_info.setText(QCoreApplication.translate("MainWindow", u"No DIY model is saved yet.", None))
        self.labelBoxBlenderInstalation_3.setText(QCoreApplication.translate("MainWindow", u"Please select the folder to save data files.", None))
        self.label_save_path.setText(QCoreApplication.translate("MainWindow", u"Save file path:", None))
        self.line_save_file_path.setText(QCoreApplication.translate("MainWindow", u"(Default)./save", None))
        self.line_save_file_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.btn_save_path.setText(QCoreApplication.translate("MainWindow", u"Select path", None))
        self.btn_save_file.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_save_answer.setText(QCoreApplication.translate("MainWindow", u"No file is saved yet.", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"System constructed by: Homo; UI style contributed by: Wanderson M. Pimenta.", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

