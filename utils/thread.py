# -*- codeing = utf-8 -*-
# @time :2022/1/2019:33
# @Author : park
# @File :thread.py
# @Software:PyCharm
import bs4 as bs4

HOST = "http://www.amazon.com"
HOST_ASIN_TPL = "{}{}".format(HOST,"gp/product/")

from PyQt5.QtCore import QThread, pyqtSignal


class NewTaskThread(QThread):

    updated = pyqtSignal(str,str,str)
    error = pyqtSignal(str,str,str)

    def __init__(self,asin,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.asin = asin

    def run(self, PROXY=None):
        try:
            url = "{}{}/".format(HOST_ASIN_TPL,self.asin)
            print(url)
            success,text,proxy_ip  = PROXY.request(url)
            if not success:
                raise Exception(text)
            soup = bs4.BeautifulSoup(text,"lxml0")
            title = soup.find(id = "title").text.strip()
            url = "{}{}/ref = dp_olp_all_mbc?ie=UTF*&condition=new".format(HOST_ASIN_TPL,self.asin)
            self.updated.emit(self.asin,title,url)
        except Exception as e:
            title = "监控项{}添加失败".format(self.asin)
            self.error.emit(self.asin,title,str(e))