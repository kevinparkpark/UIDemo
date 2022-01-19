# -*- codeing = utf-8 -*-
# @time :2022/1/1911:13
# @Author : park
# @File :example_demo.py
# @Software:PyCharm

import sys
import example_files
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = example_files.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
