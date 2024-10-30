#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    :2024/10/30 16:43:59
# @Author  :小 y 同 学
# @公众号   :小y只会写bug
# @CSDN    :https://blog.csdn.net/weixin_64989228?type=blog
# @Discript:查找轨道文件
import datetime
import os
import re
import requests
from src.Message import Message
from dateutil.parser import parse
from src.ExtractDate import *


class FindOrbit:
    def __init__(self) -> None:
        """获取轨道文件列表"""
        while not self.__get_eof_list():
            pass

    def fromSLC(self, SLCFile):
        """根据SLC文件名查找轨道文件"""
        for eof in self.eoflist:
            if os.path.splitext(eof)[1] == ".EOF":
                if SLCToDate.One(SLCFile) == EOFToDate.One(eof):
                    res = f"https://s1qc.asf.alaska.edu/aux_poeorb/{eof}"
                    return res
        return None

    def fromDate(self, date):
        """根据日期查找轨道文件"""
        for eof in self.eoflist:
            if os.path.splitext(eof)[1] == ".EOF":
                if EOFToDate.One(eof) == str(date):
                    res = f"https://s1qc.asf.alaska.edu/aux_poeorb/{eof}"
                    return res
        return None

    def __get_eof_list(self):
        Message.print_info("Getting EOF list from ASF...")
        eoflisturl = "https://s1qc.asf.alaska.edu/aux_poeorb/"
        try:
            res = requests.get(eoflisturl, timeout=20)
            self.eoflist = re.findall('href="(.*?\.EOF)">', res.text)
            print(self.eoflist)
            return True
        except Exception as e:
            Message.print_error(
                f"{str(e)}\nAn exception occurred while getting the EOF list\nRetry."
            )
            return False


if __name__ == "__main__":
    fdo = FindOrbit()
    print(
        fdo.fromSLC(
            "S1A_IW_SLC__1SDV_20141003T235924_20141003T235951_002661_002F1D_1A1D.SAFE"
        )
    )
    print(fdo.fromDate("20230929"))
