# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fgoMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_fgoMainWindow(object):
    def setupUi(self, fgoMainWindow):
        if not fgoMainWindow.objectName():
            fgoMainWindow.setObjectName(u"fgoMainWindow")
        fgoMainWindow.setFocusPolicy(Qt.StrongFocus)
        fgoMainWindow.setStyleSheet(u"QWidget{font-family:\"Microsoft YaHei UI Light\";font-size:15px}")
        self.MENU_ABOUT_ABOUT = QAction(fgoMainWindow)
        self.MENU_ABOUT_ABOUT.setObjectName(u"MENU_ABOUT_ABOUT")
        self.MENU_FILE_EXPLORER = QAction(fgoMainWindow)
        self.MENU_FILE_EXPLORER.setObjectName(u"MENU_FILE_EXPLORER")
        self.MENU_CONTROL_STAYONTOP = QAction(fgoMainWindow)
        self.MENU_CONTROL_STAYONTOP.setObjectName(u"MENU_CONTROL_STAYONTOP")
        self.MENU_CONTROL_STAYONTOP.setCheckable(True)
        self.MENU_SCRIPT_FPSUMMON = QAction(fgoMainWindow)
        self.MENU_SCRIPT_FPSUMMON.setObjectName(u"MENU_SCRIPT_FPSUMMON")
        self.MENU_SCRIPT_SYNTHESIS = QAction(fgoMainWindow)
        self.MENU_SCRIPT_SYNTHESIS.setObjectName(u"MENU_SCRIPT_SYNTHESIS")
        self.MENU_SCRIPT_SUMMONHISTORY = QAction(fgoMainWindow)
        self.MENU_SCRIPT_SUMMONHISTORY.setObjectName(u"MENU_SCRIPT_SUMMONHISTORY")
        self.MENU_SCRIPT_EXPBALL = QAction(fgoMainWindow)
        self.MENU_SCRIPT_EXPBALL.setObjectName(u"MENU_SCRIPT_EXPBALL")
        self.MENU_CONTROL_MAPKEY = QAction(fgoMainWindow)
        self.MENU_CONTROL_MAPKEY.setObjectName(u"MENU_CONTROL_MAPKEY")
        self.MENU_CONTROL_MAPKEY.setCheckable(True)
        self.MENU_SCRIPT_LOTTERY = QAction(fgoMainWindow)
        self.MENU_SCRIPT_LOTTERY.setObjectName(u"MENU_SCRIPT_LOTTERY")
        self.MENU_SCRIPT_MAILFILTER = QAction(fgoMainWindow)
        self.MENU_SCRIPT_MAILFILTER.setObjectName(u"MENU_SCRIPT_MAILFILTER")
        self.MENU_CONTROL_BENCH = QAction(fgoMainWindow)
        self.MENU_CONTROL_BENCH.setObjectName(u"MENU_CONTROL_BENCH")
        self.MENU_CONTROL_EXEC = QAction(fgoMainWindow)
        self.MENU_CONTROL_EXEC.setObjectName(u"MENU_CONTROL_EXEC")
        self.MENU_SETTINGS_DEFEATED = QAction(fgoMainWindow)
        self.MENU_SETTINGS_DEFEATED.setObjectName(u"MENU_SETTINGS_DEFEATED")
        self.MENU_SETTINGS_DEFEATED.setCheckable(True)
        self.MENU_SETTINGS_KIZUNAREISOU = QAction(fgoMainWindow)
        self.MENU_SETTINGS_KIZUNAREISOU.setObjectName(u"MENU_SETTINGS_KIZUNAREISOU")
        self.MENU_SETTINGS_KIZUNAREISOU.setCheckable(True)
        self.MENU_SETTINGS_SPECIALDROP = QAction(fgoMainWindow)
        self.MENU_SETTINGS_SPECIALDROP.setObjectName(u"MENU_SETTINGS_SPECIALDROP")
        self.MENU_ABOUT_LICENSE = QAction(fgoMainWindow)
        self.MENU_ABOUT_LICENSE.setObjectName(u"MENU_ABOUT_LICENSE")
        self.MENU_FILE_QUIT = QAction(fgoMainWindow)
        self.MENU_FILE_QUIT.setObjectName(u"MENU_FILE_QUIT")
        self.MENU_CONTROL_TRAY = QAction(fgoMainWindow)
        self.MENU_CONTROL_TRAY.setObjectName(u"MENU_CONTROL_TRAY")
        self.MENU_CONTROL_TRAY.setCheckable(True)
        self.MENU_CONTROL_169_INVOKE = QAction(fgoMainWindow)
        self.MENU_CONTROL_169_INVOKE.setObjectName(u"MENU_CONTROL_169_INVOKE")
        self.MENU_CONTROL_169_REVOKE = QAction(fgoMainWindow)
        self.MENU_CONTROL_169_REVOKE.setObjectName(u"MENU_CONTROL_169_REVOKE")
        self.MENU_CONTROL_NOTIFY = QAction(fgoMainWindow)
        self.MENU_CONTROL_NOTIFY.setObjectName(u"MENU_CONTROL_NOTIFY")
        self.MENU_CONTROL_NOTIFY.setCheckable(True)
        self.widget = QWidget(fgoMainWindow)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LAYOUT_INFO = QFormLayout()
        self.LAYOUT_INFO.setObjectName(u"LAYOUT_INFO")
        self.LAYOUT_INFO.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.LBL_APPLE = QLabel(self.widget)
        self.LBL_APPLE.setObjectName(u"LBL_APPLE")
        self.LBL_APPLE.setMaximumSize(QSize(16777215, 28))

        self.LAYOUT_INFO.setWidget(1, QFormLayout.LabelRole, self.LBL_APPLE)

        self.LAYOUT_INFO_APPLE = QHBoxLayout()
        self.LAYOUT_INFO_APPLE.setObjectName(u"LAYOUT_INFO_APPLE")
        self.CBX_APPLE = QComboBox(self.widget)
        self.CBX_APPLE.addItem("")
        self.CBX_APPLE.addItem("")
        self.CBX_APPLE.addItem("")
        self.CBX_APPLE.addItem("")
        self.CBX_APPLE.addItem("")
        self.CBX_APPLE.setObjectName(u"CBX_APPLE")

        self.LAYOUT_INFO_APPLE.addWidget(self.CBX_APPLE)

        self.TXT_APPLE = QSpinBox(self.widget)
        self.TXT_APPLE.setObjectName(u"TXT_APPLE")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TXT_APPLE.sizePolicy().hasHeightForWidth())
        self.TXT_APPLE.setSizePolicy(sizePolicy)
        self.TXT_APPLE.setContextMenuPolicy(Qt.NoContextMenu)
        self.TXT_APPLE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.TXT_APPLE.setMaximum(114514)

        self.LAYOUT_INFO_APPLE.addWidget(self.TXT_APPLE)


        self.LAYOUT_INFO.setLayout(1, QFormLayout.FieldRole, self.LAYOUT_INFO_APPLE)

        self.LBL_TEAM = QLabel(self.widget)
        self.LBL_TEAM.setObjectName(u"LBL_TEAM")

        self.LAYOUT_INFO.setWidget(0, QFormLayout.LabelRole, self.LBL_TEAM)

        self.TXT_TEAM = QSpinBox(self.widget)
        self.TXT_TEAM.setObjectName(u"TXT_TEAM")
        self.TXT_TEAM.setContextMenuPolicy(Qt.NoContextMenu)
        self.TXT_TEAM.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.TXT_TEAM.setMaximum(10)

        self.LAYOUT_INFO.setWidget(0, QFormLayout.FieldRole, self.TXT_TEAM)

        self.LBL_MAX_BATTLES = QLabel(self.widget)
        self.LBL_MAX_BATTLES.setObjectName(u"LBL_MAX_BATTLES")

        self.LAYOUT_INFO.setWidget(2, QFormLayout.LabelRole, self.LBL_MAX_BATTLES)

        self.TXT_MAX_BATTLES = QSpinBox(self.widget)
        self.TXT_MAX_BATTLES.setObjectName(u"TXT_MAX_BATTLES")
        self.TXT_MAX_BATTLES.setContextMenuPolicy(Qt.NoContextMenu)
        self.TXT_MAX_BATTLES.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.TXT_MAX_BATTLES.setMaximum(99)

        self.LAYOUT_INFO.setWidget(2, QFormLayout.FieldRole, self.TXT_MAX_BATTLES)

        self.LBL_CURRENTDEVICE = QLabel(self.widget)
        self.LBL_CURRENTDEVICE.setObjectName(u"LBL_CURRENTDEVICE")

        self.LAYOUT_INFO.setWidget(3, QFormLayout.LabelRole, self.LBL_CURRENTDEVICE)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LBL_DEVICE = QLabel(self.widget)
        self.LBL_DEVICE.setObjectName(u"LBL_DEVICE")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LBL_DEVICE.sizePolicy().hasHeightForWidth())
        self.LBL_DEVICE.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.LBL_DEVICE)

        self.BTN_CONNECT = QPushButton(self.widget)
        self.BTN_CONNECT.setObjectName(u"BTN_CONNECT")
        self.BTN_CONNECT.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.BTN_CONNECT)


        self.LAYOUT_INFO.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout)


        self.verticalLayout.addLayout(self.LAYOUT_INFO)

        self.BTN_MAIN = QPushButton(self.widget)
        self.BTN_MAIN.setObjectName(u"BTN_MAIN")
        self.BTN_MAIN.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.BTN_MAIN)

        self.LAYOUT_FUNC = QHBoxLayout()
        self.LAYOUT_FUNC.setObjectName(u"LAYOUT_FUNC")
        self.LAYOUT_FUNC_BATTLE = QVBoxLayout()
        self.LAYOUT_FUNC_BATTLE.setObjectName(u"LAYOUT_FUNC_BATTLE")
        self.BTN_BATTLE = QPushButton(self.widget)
        self.BTN_BATTLE.setObjectName(u"BTN_BATTLE")

        self.LAYOUT_FUNC_BATTLE.addWidget(self.BTN_BATTLE)

        self.BTN_CLASSIC = QPushButton(self.widget)
        self.BTN_CLASSIC.setObjectName(u"BTN_CLASSIC")
        self.BTN_CLASSIC.setCursor(QCursor(Qt.PointingHandCursor))

        self.LAYOUT_FUNC_BATTLE.addWidget(self.BTN_CLASSIC)


        self.LAYOUT_FUNC.addLayout(self.LAYOUT_FUNC_BATTLE)

        self.LAYOUT_FUMC_MAIN = QVBoxLayout()
        self.LAYOUT_FUMC_MAIN.setObjectName(u"LAYOUT_FUMC_MAIN")
        self.BTN_PAUSE = QPushButton(self.widget)
        self.BTN_PAUSE.setObjectName(u"BTN_PAUSE")
        self.BTN_PAUSE.setEnabled(False)
        self.BTN_PAUSE.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_PAUSE.setCheckable(True)

        self.LAYOUT_FUMC_MAIN.addWidget(self.BTN_PAUSE)

        self.BTN_STOP = QPushButton(self.widget)
        self.BTN_STOP.setObjectName(u"BTN_STOP")
        self.BTN_STOP.setEnabled(False)
        self.BTN_STOP.setCursor(QCursor(Qt.PointingHandCursor))

        self.LAYOUT_FUMC_MAIN.addWidget(self.BTN_STOP)


        self.LAYOUT_FUNC.addLayout(self.LAYOUT_FUMC_MAIN)

        self.LAYOUT_FUNC_CONTROL = QVBoxLayout()
        self.LAYOUT_FUNC_CONTROL.setObjectName(u"LAYOUT_FUNC_CONTROL")
        self.BTN_SCREENSHOT = QPushButton(self.widget)
        self.BTN_SCREENSHOT.setObjectName(u"BTN_SCREENSHOT")
        self.BTN_SCREENSHOT.setCursor(QCursor(Qt.PointingHandCursor))

        self.LAYOUT_FUNC_CONTROL.addWidget(self.BTN_SCREENSHOT)

        self.BTN_STOPLATER = QPushButton(self.widget)
        self.BTN_STOPLATER.setObjectName(u"BTN_STOPLATER")
        self.BTN_STOPLATER.setEnabled(False)
        self.BTN_STOPLATER.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_STOPLATER.setCheckable(True)

        self.LAYOUT_FUNC_CONTROL.addWidget(self.BTN_STOPLATER)


        self.LAYOUT_FUNC.addLayout(self.LAYOUT_FUNC_CONTROL)


        self.verticalLayout.addLayout(self.LAYOUT_FUNC)

        fgoMainWindow.setCentralWidget(self.widget)
        self.MENU = QMenuBar(fgoMainWindow)
        self.MENU.setObjectName(u"MENU")
        self.MENU_ABOUT = QMenu(self.MENU)
        self.MENU_ABOUT.setObjectName(u"MENU_ABOUT")
        self.MENU_FILE = QMenu(self.MENU)
        self.MENU_FILE.setObjectName(u"MENU_FILE")
        self.MENU_SCRIPT = QMenu(self.MENU)
        self.MENU_SCRIPT.setObjectName(u"MENU_SCRIPT")
        self.MENU_CONTROL = QMenu(self.MENU)
        self.MENU_CONTROL.setObjectName(u"MENU_CONTROL")
        self.MENU_CONTROL_169 = QMenu(self.MENU_CONTROL)
        self.MENU_CONTROL_169.setObjectName(u"MENU_CONTROL_169")
        self.MENU_SETTINGS = QMenu(self.MENU)
        self.MENU_SETTINGS.setObjectName(u"MENU_SETTINGS")
        fgoMainWindow.setMenuBar(self.MENU)
        self.STATUS = QStatusBar(fgoMainWindow)
        self.STATUS.setObjectName(u"STATUS")
        fgoMainWindow.setStatusBar(self.STATUS)
        QWidget.setTabOrder(self.TXT_TEAM, self.TXT_MAX_BATTLES)
        QWidget.setTabOrder(self.TXT_MAX_BATTLES, self.CBX_APPLE)
        QWidget.setTabOrder(self.CBX_APPLE, self.TXT_APPLE)
        QWidget.setTabOrder(self.TXT_APPLE, self.BTN_CONNECT)
        QWidget.setTabOrder(self.BTN_CONNECT, self.BTN_MAIN)
        QWidget.setTabOrder(self.BTN_MAIN, self.BTN_BATTLE)
        QWidget.setTabOrder(self.BTN_BATTLE, self.BTN_CLASSIC)
        QWidget.setTabOrder(self.BTN_CLASSIC, self.BTN_PAUSE)
        QWidget.setTabOrder(self.BTN_PAUSE, self.BTN_STOP)
        QWidget.setTabOrder(self.BTN_STOP, self.BTN_SCREENSHOT)
        QWidget.setTabOrder(self.BTN_SCREENSHOT, self.BTN_STOPLATER)

        self.MENU.addAction(self.MENU_FILE.menuAction())
        self.MENU.addAction(self.MENU_SCRIPT.menuAction())
        self.MENU.addAction(self.MENU_SETTINGS.menuAction())
        self.MENU.addAction(self.MENU_CONTROL.menuAction())
        self.MENU.addAction(self.MENU_ABOUT.menuAction())
        self.MENU_ABOUT.addAction(self.MENU_ABOUT_ABOUT)
        self.MENU_ABOUT.addAction(self.MENU_ABOUT_LICENSE)
        self.MENU_FILE.addAction(self.MENU_FILE_EXPLORER)
        self.MENU_SCRIPT.addAction(self.MENU_SCRIPT_FPSUMMON)
        self.MENU_SCRIPT.addAction(self.MENU_SCRIPT_LOTTERY)
        self.MENU_SCRIPT.addAction(self.MENU_SCRIPT_MAILFILTER)
        self.MENU_SCRIPT.addAction(self.MENU_SCRIPT_SYNTHESIS)
        self.MENU_SCRIPT.addAction(self.MENU_SCRIPT_SUMMONHISTORY)
        self.MENU_SCRIPT.addAction(self.MENU_SCRIPT_EXPBALL)
        self.MENU_CONTROL.addAction(self.MENU_CONTROL_STAYONTOP)
        self.MENU_CONTROL.addAction(self.MENU_CONTROL_TRAY)
        self.MENU_CONTROL.addSeparator()
        self.MENU_CONTROL.addAction(self.MENU_CONTROL_MAPKEY)
        self.MENU_CONTROL.addAction(self.MENU_CONTROL_169.menuAction())
        self.MENU_CONTROL.addAction(self.MENU_CONTROL_NOTIFY)
        self.MENU_CONTROL.addSeparator()
        self.MENU_CONTROL.addAction(self.MENU_CONTROL_BENCH)
        self.MENU_CONTROL.addAction(self.MENU_CONTROL_EXEC)
        self.MENU_CONTROL_169.addAction(self.MENU_CONTROL_169_INVOKE)
        self.MENU_CONTROL_169.addAction(self.MENU_CONTROL_169_REVOKE)
        self.MENU_SETTINGS.addAction(self.MENU_SETTINGS_DEFEATED)
        self.MENU_SETTINGS.addAction(self.MENU_SETTINGS_KIZUNAREISOU)
        self.MENU_SETTINGS.addAction(self.MENU_SETTINGS_SPECIALDROP)

        self.retranslateUi(fgoMainWindow)
        self.BTN_CLASSIC.clicked.connect(fgoMainWindow.runClassic)
        self.BTN_MAIN.clicked.connect(fgoMainWindow.runMain)
        self.BTN_SCREENSHOT.clicked.connect(fgoMainWindow.screenshot)
        self.BTN_PAUSE.clicked["bool"].connect(fgoMainWindow.pause)
        self.BTN_STOP.clicked.connect(fgoMainWindow.stop)
        self.BTN_CONNECT.clicked.connect(fgoMainWindow.connectDevice)
        self.MENU_FILE_EXPLORER.triggered.connect(fgoMainWindow.explorerHere)
        self.MENU_ABOUT_ABOUT.triggered.connect(fgoMainWindow.about)
        self.MENU_SCRIPT_FPSUMMON.triggered.connect(fgoMainWindow.runFpSummon)
        self.MENU_SCRIPT_SYNTHESIS.triggered.connect(fgoMainWindow.runSynthesis)
        self.MENU_SCRIPT_SUMMONHISTORY.triggered.connect(fgoMainWindow.runSummonHistory)
        self.MENU_SCRIPT_EXPBALL.triggered.connect(fgoMainWindow.expBall)
        self.MENU_CONTROL_MAPKEY.triggered["bool"].connect(fgoMainWindow.mapKey)
        self.BTN_STOPLATER.clicked["bool"].connect(fgoMainWindow.stopLater)
        self.MENU_SCRIPT_LOTTERY.triggered.connect(fgoMainWindow.runLottery)
        self.MENU_SCRIPT_MAILFILTER.triggered.connect(fgoMainWindow.runMail)
        self.MENU_CONTROL_BENCH.triggered.connect(fgoMainWindow.bench)
        self.MENU_CONTROL_EXEC.triggered.connect(fgoMainWindow.exec)
        self.MENU_SETTINGS_SPECIALDROP.triggered.connect(fgoMainWindow.stopOnSpecialDrop)
        self.MENU_ABOUT_LICENSE.triggered.connect(fgoMainWindow.license)
        self.MENU_CONTROL_169_INVOKE.triggered.connect(fgoMainWindow.invoke169)
        self.MENU_CONTROL_169_REVOKE.triggered.connect(fgoMainWindow.revoke169)
        self.BTN_BATTLE.clicked.connect(fgoMainWindow.runBattle)

        self.CBX_APPLE.setCurrentIndex(0)

    # setupUi

    def retranslateUi(self, fgoMainWindow):
        fgoMainWindow.setWindowTitle(QCoreApplication.translate("fgoMainWindow", u"FGO-py - hgjazhgj", None))
        self.MENU_ABOUT_ABOUT.setText(QCoreApplication.translate("fgoMainWindow", u"\u5173\u4e8eFGO-py", None))
        self.MENU_FILE_EXPLORER.setText(QCoreApplication.translate("fgoMainWindow", u"\u8d44\u6e90\u7ba1\u7406\u5668", None))
        self.MENU_CONTROL_STAYONTOP.setText(QCoreApplication.translate("fgoMainWindow", u"\u7a97\u53e3\u7f6e\u9876", None))
        self.MENU_SCRIPT_FPSUMMON.setText(QCoreApplication.translate("fgoMainWindow", u"\u62bd\u53cb\u60c5", None))
#if QT_CONFIG(statustip)
        self.MENU_SCRIPT_FPSUMMON.setStatusTip(QCoreApplication.translate("fgoMainWindow", u"\u5148\u62bd\u4e00\u53d1\u53cb\u60c5\u5341\u8fde,\u5728\u7ed3\u7b97\u754c\u9762\u8fd0\u884c\u672c\u529f\u80fd", None))
#endif // QT_CONFIG(statustip)
        self.MENU_SCRIPT_SYNTHESIS.setText(QCoreApplication.translate("fgoMainWindow", u"\u5f3a\u5316", None))
#if QT_CONFIG(statustip)
        self.MENU_SCRIPT_SYNTHESIS.setStatusTip(QCoreApplication.translate("fgoMainWindow", u"\u5728\u9009\u62e9\u4e86\u5f3a\u5316\u5bf9\u8c61\u672a\u9009\u62e9\u5f3a\u5316\u6750\u6599\u7684\u754c\u9762\u8fd0\u884c\u672c\u529f\u80fd", None))
#endif // QT_CONFIG(statustip)
        self.MENU_SCRIPT_SUMMONHISTORY.setText(QCoreApplication.translate("fgoMainWindow", u"\u53ec\u5524\u8bb0\u5f55", None))
#if QT_CONFIG(statustip)
        self.MENU_SCRIPT_SUMMONHISTORY.setStatusTip(QCoreApplication.translate("fgoMainWindow", u"\u7edf\u8ba1\u5bfc\u51fa\u53ec\u5524\u8bb0\u5f55,\u5728\u62bd\u5361\u8bb0\u5f55\u9875\u9762\u8fd0\u884c", None))
#endif // QT_CONFIG(statustip)
        self.MENU_SCRIPT_EXPBALL.setText(QCoreApplication.translate("fgoMainWindow", u"\u6413\u4e38\u5b50", None))
#if QT_CONFIG(statustip)
        self.MENU_SCRIPT_EXPBALL.setStatusTip(QCoreApplication.translate("fgoMainWindow", u"\u628a\u82e5\u5e72\u5f20\u4f4e\u661f\u793c\u88c5\u5408\u5e76\u6210\u4e00\u4e2a", None))
#endif // QT_CONFIG(statustip)
        self.MENU_CONTROL_MAPKEY.setText(QCoreApplication.translate("fgoMainWindow", u"\u52a0\u8f7d\u6309\u952e\u6620\u5c04", None))
        self.MENU_SCRIPT_LOTTERY.setText(QCoreApplication.translate("fgoMainWindow", u"\u62bd\u5956\u6c60", None))
        self.MENU_SCRIPT_MAILFILTER.setText(QCoreApplication.translate("fgoMainWindow", u"\u6e05\u7406\u90ae\u7bb1", None))
        self.MENU_CONTROL_BENCH.setText(QCoreApplication.translate("fgoMainWindow", u"Bench", None))
        self.MENU_CONTROL_EXEC.setText(QCoreApplication.translate("fgoMainWindow", u"Execute", None))
        self.MENU_SETTINGS_DEFEATED.setText(QCoreApplication.translate("fgoMainWindow", u"\u6218\u8d25\u64a4\u9000\u65f6\u7ec8\u6b62\u6218\u6597", None))
        self.MENU_SETTINGS_KIZUNAREISOU.setText(QCoreApplication.translate("fgoMainWindow", u"\u83b7\u5f97\u7f81\u7eca\u793c\u88c5\u65f6\u7ec8\u6b62\u6218\u6597", None))
        self.MENU_SETTINGS_SPECIALDROP.setText(QCoreApplication.translate("fgoMainWindow", u"\u82e5\u5e72\u7279\u6b8a\u6389\u843d\u540e\u7ec8\u6b62\u6218\u6597", None))
        self.MENU_ABOUT_LICENSE.setText(QCoreApplication.translate("fgoMainWindow", u"\u4f7f\u7528\u8bb8\u53ef", None))
        self.MENU_FILE_QUIT.setText(QCoreApplication.translate("fgoMainWindow", u"\u9000\u51fa", None))
        self.MENU_CONTROL_TRAY.setText(QCoreApplication.translate("fgoMainWindow", u"\u5173\u95ed\u5230\u6258\u76d8", None))
        self.MENU_CONTROL_169_INVOKE.setText(QCoreApplication.translate("fgoMainWindow", u"\u8c03\u6574\u4e3a16:9", None))
        self.MENU_CONTROL_169_REVOKE.setText(QCoreApplication.translate("fgoMainWindow", u"\u6062\u590d\u539f\u5206\u8fa8\u7387", None))
        self.MENU_CONTROL_NOTIFY.setText(QCoreApplication.translate("fgoMainWindow", u"\u6d88\u606f\u63a8\u9001", None))
        self.LBL_APPLE.setText(QCoreApplication.translate("fgoMainWindow", u"\u82f9\u679c", None))
        self.CBX_APPLE.setItemText(0, QCoreApplication.translate("fgoMainWindow", u"\u91d1", None))
        self.CBX_APPLE.setItemText(1, QCoreApplication.translate("fgoMainWindow", u"\u94f6", None))
        self.CBX_APPLE.setItemText(2, QCoreApplication.translate("fgoMainWindow", u"\u9752", None))
        self.CBX_APPLE.setItemText(3, QCoreApplication.translate("fgoMainWindow", u"\u94dc", None))
        self.CBX_APPLE.setItemText(4, QCoreApplication.translate("fgoMainWindow", u"\u5f69", None))

#if QT_CONFIG(statustip)
        self.CBX_APPLE.setStatusTip(QCoreApplication.translate("fgoMainWindow", u"\u8981\u5403\u7684\u82f9\u679c\u79cd\u7c7b,\u5728\u8fd0\u884c\u524d\u8bbe\u7f6e", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.TXT_APPLE.setStatusTip(QCoreApplication.translate("fgoMainWindow", u"\u8981\u5403\u7684\u82f9\u679c\u6570\u91cf,\u5728\u8fd0\u884c\u524d\u8bbe\u7f6e", None))
#endif // QT_CONFIG(statustip)
        self.LBL_TEAM.setText(QCoreApplication.translate("fgoMainWindow", u"\u7f16\u961f\u4f4d\u7f6e", None))
#if QT_CONFIG(statustip)
        self.TXT_TEAM.setStatusTip(QCoreApplication.translate("fgoMainWindow", u"\u6240\u9009\u7f16\u961f\u5728\u961f\u4f0d\u7f16\u6210\u754c\u9762\u7684\u4f4d\u7f6e,\u4ece\u5de6\u5230\u53f31-10,0\u4e3a\u65e0\u6548", None))
#endif // QT_CONFIG(statustip)
        self.LBL_MAX_BATTLES.setText(QCoreApplication.translate("fgoMainWindow", u"\u9a6c\u514b\u65af\u6218\u6597", None))
#if QT_CONFIG(statustip)
        self.TXT_MAX_BATTLES.setStatusTip(QCoreApplication.translate("fgoMainWindow", u"\u505c\u6b62\u524d\u7684\u6700\u591a\u6218\u6597\u6b21\u6570\uff0c0 \u8868\u793a\u4e0d\u505c\u6218\u6597", None))
#endif // QT_CONFIG(statustip)
        self.LBL_CURRENTDEVICE.setText(QCoreApplication.translate("fgoMainWindow", u"\u5f53\u524d\u8bbe\u5907", None))
#if QT_CONFIG(statustip)
        self.BTN_CONNECT.setStatusTip(QCoreApplication.translate("fgoMainWindow", u"\u8fde\u63a5\u5230\u8bbe\u5907", None))
#endif // QT_CONFIG(statustip)
        self.BTN_CONNECT.setText(QCoreApplication.translate("fgoMainWindow", u"\u66f4\u6539", None))
#if QT_CONFIG(statustip)
        self.BTN_MAIN.setStatusTip(QCoreApplication.translate("fgoMainWindow", u"\u5728\u5173\u5361\u5217\u8868\u754c\u9762\u5c06\u8981\u5237\u7684\u5173\u5361\u7f6e\u4e8e\u7b2c\u4e00\u4e2a\u6765\u6e05\u7a7a\u4f53\u529b", None))
#endif // QT_CONFIG(statustip)
        self.BTN_MAIN.setText(QCoreApplication.translate("fgoMainWindow", u"\u809d!", None))
#if QT_CONFIG(statustip)
        self.BTN_BATTLE.setStatusTip(QCoreApplication.translate("fgoMainWindow", u"\u5b8c\u6210\u5f53\u524d\u6218\u6597", None))
#endif // QT_CONFIG(statustip)
        self.BTN_BATTLE.setText(QCoreApplication.translate("fgoMainWindow", u"\u5b8c\u6210\u6218\u6597", None))
#if QT_CONFIG(statustip)
        self.BTN_CLASSIC.setStatusTip(QCoreApplication.translate("fgoMainWindow", u"\u57fa\u4e8e\u7ecf\u5178\u6218\u6597\u7684\u6e05\u7a7a\u4f53\u529b", None))
#endif // QT_CONFIG(statustip)
        self.BTN_CLASSIC.setText(QCoreApplication.translate("fgoMainWindow", u"\u9648\u5e74\u8001\u809d", None))
#if QT_CONFIG(statustip)
        self.BTN_PAUSE.setStatusTip(QCoreApplication.translate("fgoMainWindow", u"\u6682\u505c/\u7ee7\u7eed\u6218\u6597", None))
#endif // QT_CONFIG(statustip)
        self.BTN_PAUSE.setText(QCoreApplication.translate("fgoMainWindow", u"\u6302\u8d77\u6218\u6597", None))
#if QT_CONFIG(statustip)
        self.BTN_STOP.setStatusTip(QCoreApplication.translate("fgoMainWindow", u"\u7acb\u523b\u7ec8\u6b62\u6218\u6597", None))
#endif // QT_CONFIG(statustip)
        self.BTN_STOP.setText(QCoreApplication.translate("fgoMainWindow", u"\u7ec8\u6b62\u6218\u6597", None))
#if QT_CONFIG(statustip)
        self.BTN_SCREENSHOT.setStatusTip(QCoreApplication.translate("fgoMainWindow", u"\u68c0\u67e5\u622a\u56fe\u786e\u5b9a\u8fde\u63a5\u5efa\u7acb", None))
#endif // QT_CONFIG(statustip)
        self.BTN_SCREENSHOT.setText(QCoreApplication.translate("fgoMainWindow", u"\u68c0\u67e5\u622a\u56fe", None))
#if QT_CONFIG(statustip)
        self.BTN_STOPLATER.setStatusTip(QCoreApplication.translate("fgoMainWindow", u"\u5728\u5b8c\u6210\u82e5\u5e72\u573a\u6218\u6597\u540e\u7ec8\u6b62\u6218\u6597", None))
#endif // QT_CONFIG(statustip)
        self.BTN_STOPLATER.setText(QCoreApplication.translate("fgoMainWindow", u"\u9884\u7ea6\u7ec8\u6b62", None))
        self.MENU_ABOUT.setTitle(QCoreApplication.translate("fgoMainWindow", u"\u5173\u4e8e", None))
        self.MENU_FILE.setTitle(QCoreApplication.translate("fgoMainWindow", u"\u6587\u4ef6", None))
        self.MENU_SCRIPT.setTitle(QCoreApplication.translate("fgoMainWindow", u"\u7a0b\u5e8f", None))
        self.MENU_CONTROL.setTitle(QCoreApplication.translate("fgoMainWindow", u"\u63a7\u5236", None))
        self.MENU_CONTROL_169.setTitle(QCoreApplication.translate("fgoMainWindow", u"\u5168\u9762\u5c4f\u9002\u914d", None))
        self.MENU_SETTINGS.setTitle(QCoreApplication.translate("fgoMainWindow", u"\u8bbe\u7f6e", None))
    # retranslateUi

