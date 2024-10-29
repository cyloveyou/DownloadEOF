#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    :2024/10/29 23:55:13
# @Author  :小 y 同 学
# @公众号   :小y只会写bug
# @CSDN    :https://blog.csdn.net/weixin_64989228?type=blog
# @Discript:从SLC文件名中提取日期

import re


def SLCToDate(SLCFile):
    """从SLC文件名中提取日期

    Args:
        SLCFile (_type_): SLC文件路径
    """
    temp = re.findall("_(\d{8})T", SLCFile)
    SLCdate = temp[0]  # 0是数据起始时间  1是数据结束时间
    return SLCdate


def SLCListToDate(SLCList) -> list:
    """从SLC文件列表中提取日期

    Args:
        SLCList (_type_): SLC文件列表
    """
    return list(map(SLCToDate, SLCList))


if __name__ == "__main__":
    print(
        SLCToDate(
            "S1A_IW_SLC__1SDV_20141003T235924_20141003T235951_002661_002F1D_1A1D.SAFE"
        )
    )
