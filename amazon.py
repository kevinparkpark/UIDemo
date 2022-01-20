# -*- codeing = utf-8 -*-
# @time :2022/1/2014:31
# @Author : park
# @File :amazon.py
# @Software:PyCharm
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, \
    QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """窗体元素生成"""
        self.setWindowTitle('亚马逊检测平台')
        self.resize(1228, 550)

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        # 添加按钮
        # 垂直布局
        layout = QVBoxLayout()

        layout.addLayout(self.init_form())
        layout.addLayout(self.init_header())

        # 表格
        layout.addLayout(self.init_table())

        layout.addStretch(1)
        self.setLayout(layout)
        self.show()

    def init_header(self):
        # 顶部布局
        header = QHBoxLayout()

        btn_start = QPushButton("开始")
        btn_start.clicked.connect(self.event_start_click)
        header.addWidget(btn_start)

        btn_stop = QPushButton("结束")
        btn_stop.clicked.connect(self.event_stop_click)
        header.addWidget(btn_stop)

        header.addStretch(1)
        return header

    def init_form(self):
        # 输入框
        form = QHBoxLayout()

        self.txt_asin = txt_asin = QLineEdit()
        txt_asin.setPlaceholderText("请输入商品ASIN")
        form.addWidget(txt_asin)
        btn_add = QPushButton("添加")
        btn_add.clicked.connect(self.event_add_click)
        form.addWidget(btn_add)
        return form

    def init_table(self):
        table = QHBoxLayout()
        table_widget = QTableWidget(0, 8)
        # 生成表头
        table_header_list = [
            {"field": "asin", "text": "ASIN", 'width': 120},
            {"field": "title", "text": "标题", 'width': 150},
            {"field": "url", "text": "URL", 'width': 120},
            {"field": "price", "text": "底价", 'width': 120},
            {"field": "success", "text": "成功次数", 'width': 120},
            {"field": "status", "text": "状态", 'width': 120},
            {"field": "frequency", "text": "频率(N秒/次)", 'width': 120},
        ]

        for index, info in enumerate(table_header_list):
            # 设置表头
            table_widget.setColumnWidth(index, info['width'])
            item = QTableWidgetItem()
            item.setText(info['text'])
            table_widget.setHorizontalHeaderItem(index, item)

        # 创建表内容
        db_data_list = [
            ["xx", "xx", "xx", "xx", "xx", "xx", "xx", "xx"],
            ["oo", "oo", "oo", "oo", "oo", "oo", "oo", "oo"],
        ]

        current_row_count = table_widget.rowCount()
        for item in db_data_list:
            # 原来基础上增加一行
            table_widget.insertRow(current_row_count)
            self.creat_row(table_widget, item, current_row_count)
            current_row_count += 1

        table.addWidget(table_widget)
        return table

    def creat_row(self, table_widget, item, new_row_index):
        for column, ele in enumerate(item):
            cell = QTableWidgetItem(str(ele))
            if column in[0,4,5,6]:
                #不可以被修改
                cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table_widget.setItem(new_row_index, column, cell)

    def event_start_click(self):
        QMessageBox.warning(self, "错误", "点击开始")

    def event_stop_click(self):
        QMessageBox.warning(self, "错误", "点击结束")

    def event_add_click(self):
        QMessageBox.warning(self, "错误", "点击结束")
        # 获取数据
        text = self.txt_asin.text()
        print(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
