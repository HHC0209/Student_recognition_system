# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1600, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet("\n"
"#tab_1, #tab_2 {\n"
"    background-color: rgb(50, 50, 50);\n"
"    color: rgb(255, 255, 255);\n"
"    font:  \"楷体\";\n"
"    border-image: url(\'./img/background.jpg\');\n"
"}")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setStyleSheet("")
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(0, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_title_1 = QtWidgets.QLabel(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title_1.sizePolicy().hasHeightForWidth())
        self.label_title_1.setSizePolicy(sizePolicy)
        self.label_title_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_title_1.setStyleSheet("font: 25pt \"楷体\";\n"
"/*color: rgb(173,65,80); */\n"
"font: bold;\n"
"color: rgb(172,66,80);")
        self.label_title_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_1.setObjectName("label_title_1")
        self.verticalLayout_2.addWidget(self.label_title_1)
        self.label_player_1 = QtWidgets.QLabel(self.tab_1)
        self.label_player_1.setStyleSheet("font: 15pt \"楷体\";\n"
"color: rgb(172,66,80);\n"
"")
        self.label_player_1.setObjectName("label_player_1")
        self.verticalLayout_2.addWidget(self.label_player_1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_stu_photo_1 = QtWidgets.QLabel(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_stu_photo_1.sizePolicy().hasHeightForWidth())
        self.label_stu_photo_1.setSizePolicy(sizePolicy)
        self.label_stu_photo_1.setMinimumSize(QtCore.QSize(360, 480))
        self.label_stu_photo_1.setStyleSheet("/*background: rgb(149, 25, 30);*/")
        self.label_stu_photo_1.setText("")
        self.label_stu_photo_1.setObjectName("label_stu_photo_1")
        self.horizontalLayout_3.addWidget(self.label_stu_photo_1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.bottom_tools_1 = QtWidgets.QHBoxLayout()
        self.bottom_tools_1.setObjectName("bottom_tools_1")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_tools_1.addItem(spacerItem2)
        self.db_fdy_1 = QtWidgets.QComboBox(self.tab_1)
        self.db_fdy_1.setMinimumSize(QtCore.QSize(120, 0))
        self.db_fdy_1.setStyleSheet("/*background-color: rgb(149,25,30);*/\n"
"font: 9pt \"楷体\";")
        self.db_fdy_1.setEditable(True)
        self.db_fdy_1.setObjectName("db_fdy_1")
        self.bottom_tools_1.addWidget(self.db_fdy_1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_tools_1.addItem(spacerItem3)
        self.btn_start_or_stop_1 = QtWidgets.QPushButton(self.tab_1)
        self.btn_start_or_stop_1.setStyleSheet("font: 9pt \"楷体\";\n"
"\n"
"/*background-color: rgb(149,25,30);*/")
        self.btn_start_or_stop_1.setObjectName("btn_start_or_stop_1")
        self.bottom_tools_1.addWidget(self.btn_start_or_stop_1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_tools_1.addItem(spacerItem4)
        self.btn_publish_1 = QtWidgets.QPushButton(self.tab_1)
        self.btn_publish_1.setStyleSheet("font: 9pt \"楷体\";\n"
"/*background-color: rgb(149,25,30);*/")
        self.btn_publish_1.setObjectName("btn_publish_1")
        self.bottom_tools_1.addWidget(self.btn_publish_1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_tools_1.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.bottom_tools_1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.verticalLayout_2.setStretch(3, 2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.label_title_2 = QtWidgets.QLabel(self.tab_2)
        self.label_title_2.setStyleSheet("font: 25pt \"楷体\";\n"
"/*color: rgb(173,65,80); */\n"
"font: bold;\n"
"color: rgb(172,66,80);")
        self.label_title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_2.setObjectName("label_title_2")
        self.verticalLayout_3.addWidget(self.label_title_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.layout_2 = QtWidgets.QVBoxLayout()
        self.layout_2.setObjectName("layout_2")
        self.label_player_2 = QtWidgets.QLabel(self.tab_2)
        self.label_player_2.setStyleSheet("font: 15pt \"楷体\";\n"
"color: rgb(172,66,80);\n"
"")
        self.label_player_2.setObjectName("label_player_2")
        self.layout_2.addWidget(self.label_player_2)
        self.label_stu_photo_2 = QtWidgets.QLabel(self.tab_2)
        self.label_stu_photo_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_stu_photo_2.sizePolicy().hasHeightForWidth())
        self.label_stu_photo_2.setSizePolicy(sizePolicy)
        self.label_stu_photo_2.setMinimumSize(QtCore.QSize(360, 480))
        self.label_stu_photo_2.setStyleSheet("/*background: rgb(149, 25, 30);*/")
        self.label_stu_photo_2.setText("")
        self.label_stu_photo_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stu_photo_2.setObjectName("label_stu_photo_2")
        self.layout_2.addWidget(self.label_stu_photo_2)
        self.horizontalLayout_2.addLayout(self.layout_2)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setStyleSheet("font: 15pt \"楷体\";\n"
"color: rgb(172,66,80);\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_4.addItem(spacerItem10)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setStyleSheet("font: 18pt \"楷体\";")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 2, 1, 1)
        self.label_character = QtWidgets.QLabel(self.tab_2)
        self.label_character.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label_character.setStyleSheet("font: 18pt \"楷体\";")
        self.label_character.setTextFormat(QtCore.Qt.AutoText)
        self.label_character.setScaledContents(False)
        self.label_character.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_character.setWordWrap(True)
        self.label_character.setObjectName("label_character")
        self.gridLayout.addWidget(self.label_character, 5, 3, 1, 1)
        self.label_class = QtWidgets.QLabel(self.tab_2)
        self.label_class.setStyleSheet("font: 18pt \"楷体\";")
        self.label_class.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_class.setObjectName("label_class")
        self.gridLayout.addWidget(self.label_class, 4, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setStyleSheet("font: 18pt \"楷体\";")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        self.label_school = QtWidgets.QLabel(self.tab_2)
        self.label_school.setStyleSheet("font: 18pt \"楷体\";")
        self.label_school.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_school.setObjectName("label_school")
        self.gridLayout.addWidget(self.label_school, 3, 3, 1, 1)
        self.label_student = QtWidgets.QLabel(self.tab_2)
        self.label_student.setStyleSheet("font: 18pt \"楷体\";")
        self.label_student.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_student.setObjectName("label_student")
        self.gridLayout.addWidget(self.label_student, 2, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setStyleSheet("font: 18pt \"楷体\";")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setStyleSheet("font: 18pt \"楷体\";")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        spacerItem11 = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_4.addItem(spacerItem11)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem13)
        self.bottom_tools_2 = QtWidgets.QHBoxLayout()
        self.bottom_tools_2.setObjectName("bottom_tools_2")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_tools_2.addItem(spacerItem14)
        self.cb_fdy_2 = QtWidgets.QComboBox(self.tab_2)
        self.cb_fdy_2.setMinimumSize(QtCore.QSize(120, 0))
        self.cb_fdy_2.setStyleSheet("/*background-color: rgb(149,25,30);*/\n"
"font: 9pt \"楷体\";")
        self.cb_fdy_2.setEditable(True)
        self.cb_fdy_2.setObjectName("cb_fdy_2")
        self.bottom_tools_2.addWidget(self.cb_fdy_2)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_tools_2.addItem(spacerItem15)
        self.btn_start_or_stop_2 = QtWidgets.QPushButton(self.tab_2)
        self.btn_start_or_stop_2.setStyleSheet("font: 9pt \"楷体\";\n"
"/*background-color: rgb(149,25,30);*/")
        self.btn_start_or_stop_2.setObjectName("btn_start_or_stop_2")
        self.bottom_tools_2.addWidget(self.btn_start_or_stop_2)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_tools_2.addItem(spacerItem16)
        self.btn_publish_2 = QtWidgets.QPushButton(self.tab_2)
        self.btn_publish_2.setStyleSheet("font: 9pt \"楷体\";\n"
"/*background-color: rgb(149,25,30);*/")
        self.btn_publish_2.setObjectName("btn_publish_2")
        self.bottom_tools_2.addWidget(self.btn_publish_2)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_tools_2.addItem(spacerItem17)
        self.verticalLayout_3.addLayout(self.bottom_tools_2)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem18)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title_1.setText(_translate("MainWindow", "学生辨识"))
        self.label_player_1.setText(_translate("MainWindow", "1号选手：徐喜春"))
        self.db_fdy_1.setCurrentText(_translate("MainWindow", "选择辅导员"))
        self.btn_start_or_stop_1.setText(_translate("MainWindow", "开始 / 暂停"))
        self.btn_publish_1.setText(_translate("MainWindow", "公布答案"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "1"))
        self.label_title_2.setText(_translate("MainWindow", "学生辨识"))
        self.label_player_2.setText(_translate("MainWindow", "1号选手：徐喜春"))
        self.label.setText(_translate("MainWindow", "学生信息"))
        self.label_5.setText(_translate("MainWindow", "性格："))
        self.label_character.setText(_translate("MainWindow", "性格活泼开朗，为人热情随和"))
        self.label_class.setText(_translate("MainWindow", "班级1"))
        self.label_4.setText(_translate("MainWindow", "班级："))
        self.label_school.setText(_translate("MainWindow", "计算机科学与工程学院"))
        self.label_student.setText(_translate("MainWindow", "学生1"))
        self.label_3.setText(_translate("MainWindow", "学院："))
        self.label_2.setText(_translate("MainWindow", "姓名："))
        self.cb_fdy_2.setCurrentText(_translate("MainWindow", "选择辅导员"))
        self.btn_start_or_stop_2.setText(_translate("MainWindow", "开始 / 暂停"))
        self.btn_publish_2.setText(_translate("MainWindow", "公布答案"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "2"))