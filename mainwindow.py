from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtWidgets import QApplication, QCheckBox, QGridLayout, QTreeWidgetItem, QLabel, QLineEdit, QDialog, QMessageBox
from PyQt5.Qt import Qt, QThread,QMutex,pyqtSignal
from ui_mainwindow import Ui_MainWindow
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QTimer
from roll_photo import roll_photo
from PictureResizer import PictureResizer
from Data import Data

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    roll_photo_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # UI设置
        self.setupUi(self)
        QtWidgets.QApplication.setStyle('Fusion')
        self.setWindowTitle('学生辨识系统')
        self.tabWidget.tabBar().hide()
        self.setWindowIcon(QIcon('./img/fav.ico'))

        self.all_fdy = ['郭瑞玉', '徐喜春', '梁文能', '冀早早', '陈逸新', '夏玲玲']
        self.db_fdy_1.addItem("选择辅导员")
        self.cb_fdy_2.addItem("选择辅导员")
        for name in self.all_fdy:
            self.db_fdy_1.addItem(name)
            self.cb_fdy_2.addItem(name)

        self.btn_start_or_stop_1.setEnabled(False)
        self.btn_publish_1.setEnabled(False)

        resizer = PictureResizer('photos')
        resizer.start()
            
        # 基本属性
        self.rolling = False             #照片是否滚动
        self.current_fdy = ''            #当前参赛辅导员
        self.current_student_selected = ''  #当前选中的学生学号（类型为  str  ,给tab2）

        self.roll_photo_event = roll_photo()
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_photo)
        self.label_player_1.setText("")
        self.label_player_2.setText("")
        self.db_fdy_1.currentIndexChanged.connect(self.change_another_fdy)

        self.cb_fdy_2.currentIndexChanged.connect(self.change_another_fdy_2)

        self.data_access = Data(self.current_fdy)
        self.current_student_info = []
        # self.current_student_photo = []
        self.roll_photo_signal.connect(self.on_btn_start_or_stop_1_clicked)


# ==================================组件接口==================================================

    # 全屏时改变形状
    def resizeEvent(self, QResizeEvent):
        self.label_player_1.setIndent(int(self.width()*0.35))
        self.label_player_1.setMargin(10)
        self.label_stu_photo_1.setFixedSize(int(self.height()/900*360), int(self.height()/900*480))
        self.label_stu_photo_2.setFixedSize(int(self.height()/900*360), int(self.height()/900*480))

    # "开始/停止"按钮
    @QtCore.pyqtSlot()
    def on_btn_start_or_stop_1_clicked(self):
      
        if not self.rolling:
            if self.current_fdy:
               
                self.timer.start(10)
                self.rolling = True
                self.current_student_selected = ''
                self.db_fdy_1.setEnabled(False)
                self.btn_publish_1.setEnabled(False)
        
        else:
            self.timer.stop()
            self.rolling = False
            self.db_fdy_1.setEnabled(True)
            self.btn_publish_1.setEnabled(True)
            self.current_student_selected = self.roll_photo_event.get_current_selected_student_id()
            print("current student id is: ", self.current_student_selected)
            

    def on_btn_start_or_stop_2_clicked(self):
        self.tabWidget.setCurrentIndex(0)
        # if self.db_fdy_1.currentText()!=self.cb_fdy_2.currentText():
        #     self.db_fdy_1.setCurrentIndex(self.cb_fdy_2.currentIndex())
        #     self.change_another_fdy()
        self.rolling = False
        self.roll_photo_signal.emit()

    @QtCore.pyqtSlot()
    def on_btn_publish_1_clicked(self):
        self.tabWidget.setCurrentIndex(1)

        # self.cb_fdy_2.setCurrentIndex(self.db_fdy_1.currentIndex())
        
        #self.cb_fdy_2.setEnabled(False)
        self.btn_publish_2.setEnabled(False)

        self.current_student_info = self.data_access.get_student_info(self.current_student_selected)
      
        self.label_student.setText(self.current_student_info[0])
        self.label_school.setText(self.current_student_info[1])
        self.label_class.setText(self.current_student_info[2])
        self.label_character.setText(self.current_student_info[3])
        student_photo_path = self.data_access.get_photo(self.current_student_selected)
        if student_photo_path != '':
            self.label_stu_photo_2.setStyleSheet("border-image: url(%s);" % student_photo_path)

        # self.current_student_photo = []

       


# ================================自定义方法=================================================
      
    # 在label中显示照片
    def show_photo(self):
        student_photo_path = self.roll_photo_event.display_photo()
        self.label_stu_photo_1.setStyleSheet("border-image: url(%s);" % student_photo_path)


    def change_another_fdy_2(self):
        if self.cb_fdy_2.currentText()!=self.current_fdy:
            self.db_fdy_1.setCurrentIndex(self.cb_fdy_2.currentIndex())
            self.tabWidget.setCurrentIndex(0)
            self.label_stu_photo_1.setStyleSheet("background: rgb(255, 255, 255);")
            self.btn_start_or_stop_1.setEnabled(True)
            self.btn_publish_1.setEnabled(False)
            if self.db_fdy_1.currentIndex() != 0:
                self.label_player_1.setText("%d号选手：%s" % (self.db_fdy_1.currentIndex(), self.db_fdy_1.currentText()))
                self.label_player_2.setText("%d号选手：%s" % (self.db_fdy_1.currentIndex(), self.db_fdy_1.currentText()))
                have_student = self.roll_photo_event.reset(self.db_fdy_1.currentText())
                self.current_fdy = self.db_fdy_1.currentText()
                self.data_access = Data(self.current_fdy)
                self.data_access.load_student_info()

                if not have_student:
                    self.btn_start_or_stop_1.setEnabled(False)

            else:
                self.current_fdy = ''
                self.label_player_1.setText("")
                self.btn_start_or_stop_1.setEnabled(False)


    # 每次改变辅导员时所有预加载动作
    def change_another_fdy(self):
        self.cb_fdy_2.setCurrentText(self.db_fdy_1.currentText())
        self.label_stu_photo_1.setStyleSheet("background: rgb(255, 255, 255);")
        self.btn_start_or_stop_1.setEnabled(True)
        self.btn_publish_1.setEnabled(False)

        if self.db_fdy_1.currentIndex() != 0 and self.db_fdy_1.currentText() != self.current_fdy:
            self.label_player_1.setText("%d号选手：%s" % (self.db_fdy_1.currentIndex(), self.db_fdy_1.currentText()))
            self.label_player_2.setText("%d号选手：%s" % (self.db_fdy_1.currentIndex(), self.db_fdy_1.currentText()))
            have_student = self.roll_photo_event.reset(self.db_fdy_1.currentText())
            self.current_fdy = self.db_fdy_1.currentText()
           

            self.data_access = Data(self.current_fdy)
            self.data_access.load_student_info()

            if not have_student:
                self.btn_start_or_stop_1.setEnabled(False)

        else:
            self.current_fdy = ''
            self.label_player_1.setText("")
            self.btn_start_or_stop_1.setEnabled(False)