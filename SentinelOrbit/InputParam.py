#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    :2024/10/30 20:42:57
# @Author  :小 y 同 学
# @公众号   :小y只会写bug
# @CSDN    :https://blog.csdn.net/weixin_64989228?type=blog
# @Discript:处理配置文件读取程序参数

from configparser import ConfigParser
import os
from src.Message import *


# def checkPath(path):
#     if os.path.isabs(path):
#         return path
#     else:
#         return os.path.abspath(path)


class inputParam:
    def __init__(self, configfile=None):
        self.userid = ""
        self.userpwd = ""
        self.inputslc = ""
        self.savepath = ""
        self.ipport = ""
        self.workers = ""

        if configfile:
            self.config = configfile
            self.__readConfig()

    def __readConfig(self):
        """读取输入参数，并初步检查合法性"""
        conf = ConfigParser()
        conf.read(self.config)
        self.userid = conf.get("ASFInfo", "userid")
        self.userpwd = conf.get("ASFInfo", "userpwd")

        self.inputslc = conf.get("SLCInfo", "inputslc")
        self.inputslc = os.path.abspath(self.inputslc)

        self.savepath = conf.get("OrbitInfo", "savepath")
        self.savepath = os.path.abspath(self.savepath)

        self.ipport = conf.get("OtherInfo", "ipport")
        if self.ipport == "":
            self.ipport = None

        self.workers = conf.get("OtherInfo", "workers")
        if str.isdigit(self.workers):
            self.workers = int(self.workers)
        else:
            Message.print_error(f"workers must be a number, but got {self.workers}.")
            self.workers = None
