# -*- codeing = utf-8 -*-
# @time :2022/1/1913:32
# @Author : park
# @File :example_files_copy.py
# @Software:PyCharm
import sys

from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QMainWindow
from example_files import Ui_MainWindow

class Run_MainWindow(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(Run_MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_7.clicked.connect(self.close)
        self.pushButton_6.clicked.connect(self.textEdit.clear)
        self.pushButton_3.clicked.connect(self.get_dir)
        self.pushButton_2.clicked.connect(self.set_dir)

    def get_dir(self):
        dir_path = QFileDialog.getExistingDirectory(self,"选择文件夹","/")
        self.lineEdit_2.setText(dir_path)

    def set_dir(self):
        self.lineEdit.setText(self.lineEdit_2.text())

    def show_message(self):
        QMessageBox.information(self,"任务信息","任务完成",QMessageBox.Yes)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = Run_MainWindow()
    MainWindow.show()
    sys.exit(app.exec())