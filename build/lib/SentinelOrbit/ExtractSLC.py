#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    :2024/10/29 19:14:18
# @Author  :小 y 同 学
# @公众号   :小y只会写bug
# @CSDN    :https://blog.csdn.net/weixin_64989228?type=blog
# @Discript:获取SLC文件名
import os
import re


class ExtractDate:
    def __init__(self):
        pass

    @staticmethod
    def form_asf_pylink(pypath: str):
        """从ASF官网下载的download...py文件中提取出SLC文件名"""
        with open(pypath, "r") as f:
            data = f.read()
            slc = re.findall("https:.*(S1.*zip)", data)
            return slc

    @staticmethod
    def from_asf_metlink(metalinkpath):
        """从ASF官网下载的download...py文件中提取出SLC文件名"""
        return ExtractDate.form_asf_pylink(metalinkpath)

    @staticmethod
    def from_slc_folder(slcpath):
        """从存放SLC数据的文件夹提取SLC文件名"""
        dirlist = os.listdir(slcpath)
        slclist = [
            i
            for i in dirlist
            if (i.endswith(".zip") or i.endswith(".SAFE")) and i.startswith("S1")
        ]
        return slclist


if __name__ == "__main__":
    print(
        ExtractDate.form_asf_pylink("./exampleData/download-all-2024-10-25_09-09-42.py")
    )
    print(
        ExtractDate.from_asf_metlink(
            "./exampleData/asf-datapool-results-2024-10-25_10-46-01.metalink"
        )
    )
    print(
        ExtractDate.from_slc_folder(
            "/media/xytx/FILEdata/xytxLinuxSwap/SBASInSAR/FHS_shuiku/SLC"
        )
    )
