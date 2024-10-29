#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    :2024/10/29 19:14:18
# @Author  :小 y 同 学
# @公众号   :小y只会写bug
# @CSDN    :https://blog.csdn.net/weixin_64989228?type=blog
# @Discript:根据输入内容提取日期


class ExtractDate:
    def __init__(self):
        pass

    def FromASFPY(self, SLC):
        temp = re.findall("_(\d{8})T", SLC)
        return temp[0]

    def From_asf_metalink(self, SLC):
        temp = re.findall("_(\d{8})T", SLC)
        return temp[0]

    def From_file_list(self, SLC):
        temp = re.findall("_(\d{8})T", SLC)
        return temp[0]

    def FileListToDate(self, SLC):
        temp = re.findall("_(\d{8})T", SLC)
        return temp[0]
