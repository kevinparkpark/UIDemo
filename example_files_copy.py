# -*- codeing = utf-8 -*-
# @time :2022/1/1913:32
# @Author : park
# @File :example_files_copy.py
# @Software:PyCharm
import sys
import translation as tra

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
        self.pushButton.clicked.connect(self.clear)
        self.pushButton_4.clicked.connect(self.translate_file)

    def get_dir(self):
        dir_path = QFileDialog.getExistingDirectory(self,"选择文件夹","/")
        self.lineEdit_2.setText(dir_path)

    def set_dir(self):
        self.lineEdit.setText(self.lineEdit_2.text())

    def show_message(self):
        QMessageBox.information(self,"任务信息","任务完成",QMessageBox.Yes)

    def clear(self):
        self.show_message()

    def translate_file(self):
        content = self.textEdit.toPlainText()
        print(repr(content).replace(",",""))
        result = tra.translate(repr(content).replace(",",""))
        result = result.replace("\ n","\r\n")
        print(result)
        self.textEdit_2.setText(result)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = Run_MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
