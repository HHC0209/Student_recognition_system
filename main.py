import sys
from PyQt5 import QtWidgets
from mainwindow import MainWindow


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())

# 将ui文件和qrc文件转化成py文件
# pyuic5 -o ui_mainwindow.py mainwindow.ui
# pyrcc5 -o resource_rc.py resource.qrc 

# pyinstaller的使用方法
# pyinstaller -F main.py --noconsole
# pyinstaller -D main.py --noconsole

# 加在spec里面
# import sys
# sys.setrecursionlimit(5000)

# TODO list
