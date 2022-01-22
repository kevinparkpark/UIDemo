# -*- codeing = utf-8 -*-
# @time :2022/1/2014:31
# @Author : park
# @File :amazon.py
# @Software:PyCharm
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, \
    QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit, QMessageBox, \
    QTableWidget, QTableWidgetItem,QLabel

from utils.database import DB
from utils.thread import NewTaskThread


class MainWindow(QWidget):
    STATUS_MAPPING = {
        0:"初始化中",
        1:"待执行",
        2:"正在执行",
        3:"完成并提醒",
        10:"异常并停止",
        11:"初始化失败",
    }

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

        layout.addLayout(self.init_footer())

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
        self.table_widget = table_widget = QTableWidget(0, 7)
        # 生成表头
        table_header_list = [
            {"field": "asin", "text": "ASIN", 'width': 120},
            {"field": "title", "text": "标题", 'width': 150},
            {"field": "url", "text": "URL", 'width': 400},
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
        db_data_list = DB.CACHE_LIST

        current_row_count = table_widget.rowCount()
        for item in db_data_list:
            # 原来基础上增加一行
            table_widget.insertRow(current_row_count)
            self.creat_row(table_widget, item, current_row_count)
            current_row_count += 1

        table.addWidget(table_widget)
        return table

    def init_footer(self):
        footer = QHBoxLayout()
        self.label_status = label_status = QLabel("未检测",self)
        footer.addWidget(label_status)

        footer_config = QHBoxLayout()
        footer_config.addStretch(1)

        btn_reinit = QPushButton("重新初始化")
        footer_config.addWidget(btn_reinit,0,Qt.AlignRight)
        # btn_reinit.clicked.connect(self.event_reinit_click)

        btn_recheck = QPushButton("重新检测")
        footer_config.addWidget(btn_recheck,0,Qt.AlignRight)
        # btn_recheck.clicked.connect(self.event_recheck_click)

        btn_reset_count = QPushButton("次数清零")
        footer_config.addWidget(btn_reset_count, 0, Qt.AlignRight)
        # btn_reset_count.clicked.connect(self.event_reset_count_click)

        btn_delete = QPushButton("删除检测项")
        footer_config.addWidget(btn_delete, 0, Qt.AlignRight)
        # btn_delete.clicked.connect(self.event_delete_click)

        btn_alertr = QPushButton("SMTP报警配置")
        footer_config.addWidget(btn_alertr, 0, Qt.AlignRight)
        # btn_alertr.clicked.connect(self.event_alert_click)

        btn_proxy = QPushButton("代理IP")
        footer_config.addWidget(btn_proxy, 0, Qt.AlignRight)
        # btn_proxy.clicked.connect(self.event_proxy_click)

        footer.addLayout(footer_config)
        return footer

    def creat_row(self, table_widget, item, new_row_index):
        for column, ele in enumerate(item):

            text = self.STATUS_MAPPING[item[column]] if column ==6 else item[column]

            cell = QTableWidgetItem(str(text))
            if column in[0,4,5,6]:
                #不可以被修改
                cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table_widget.setItem(new_row_index, column, cell)

    def event_start_click(self):
        QMessageBox.warning(self, "错误", "点击开始")

    def event_stop_click(self):
        QMessageBox.warning(self, "错误", "点击结束")

    def event_add_click(self):
        # 获取数据
        text = self.txt_asin.text()
        if not text:
            QMessageBox.warning(self,"错误","商品ASIN输入错误！")
            return

        text = text.replace("，",",")
        asin_price_list = text.split(",")

        #获取当前表格总共有多少行
        current_row_index = self.table_widget.rowCount()

        for item in asin_price_list:
            data_pair = item.split("=")
            if len(data_pair) !=2:
                continue
            try:
                asin,price = data_pair
                asin = asin.strip()
                price = float(price.strip())
            except Exception as e:
                QMessageBox.warning(self,"错误","商品ASIN输入错误！")
                return

            #ASIN已存在，自动忽略不添加
            if DB.get_by_asin(asin):
                continue

            #表格添加，数据库插入
            new_row_data_list = [asin,"","",price,0,0,0,5]
            DB.add(new_row_data_list)

            self.table_widget.insertRow(current_row_index)
            self.creat_row(self.table_widget,new_row_data_list,current_row_index)

            #线程
            thread = NewTaskThread(asin,self)
            thread.start()
            current_row_index +=1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
