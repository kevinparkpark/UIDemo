# -*- codeing = utf-8 -*-
# @time :2022/1/2018:03
# @Author : park
# @File :database.py
# @Software:PyCharm
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class FileDBHleper(object):
    CACHE_LIST = []
    CACHE_DICT = []

    def __init__(self,file_name):
        folder = os.path.join(BASE_DIR,"db")
        if not os.path.exists(folder):
            os.makedirs(folder)
        self.db_file_path = os.path.join(BASE_DIR,"db",file_name)

        self.initial()

    def initial(self):
        if not os.path.exists(self.db_file_path):
            return
        file_object = open(self.db_file_path,mode = 'r',encoding = "utf-8")
        data = json.load(file_object)
        file_object.close()

        self.CACHE_LIST = data
        self.CACHE_DICT = {item[0]:item for item in data}

    def update_status_by_index(self,index,status):
        self.CACHE_LIST[index][6] = status
        self.write(self.CACHE_LIST)

    def write(self,data):
        file_object = open(self.db_file_path,mode='w',encoding = 'utf-8')
        json.dump(data,file_object)
        file_object.close()

    def add(self,row_data_list):
        self.CACHE_LIST.append(row_data_list)
        self.CACHE_DICT[row_data_list[0]] = row_data_list
        self.write(self.CACHE_LIST)

DB = FileDBHleper("db.json")