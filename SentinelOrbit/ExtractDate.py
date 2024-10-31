#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    :2024/10/29 23:55:13
# @Author  :小 y 同 学
# @公众号   :小y只会写bug
# @CSDN    :https://blog.csdn.net/weixin_64989228?type=blog
# @Discript:处理日期

import re
import datetime
from dateutil.parser import parse


class SLCToDate:
    def One(SLCfile) -> str:
        """从SLC文件名中提取日期

        Args:
            SLCFile (_type_): SLC文件路径
        """
        temp = re.findall("_(\d{8})T", SLCfile)
        SLCdate = temp[0]  # 0是数据起始时间  1是数据结束时间
        return SLCdate

    @classmethod
    def AList(cls, SLClist) -> list:
        """从SLC文件列表中提取日期

        Args:
            SLCList (_type_): SLC文件列表
        """
        return list(map(cls.AList, SLClist))


class EOFToDate:
    def __init__(self) -> None:
        pass

    def One(EOFfile) -> str:
        EOFdate = re.findall("V(\d+)T", EOFfile)[0]  # 轨道的起始时间
        EOFdate = parse(EOFdate) + datetime.timedelta(days=+1)  # 加一天表示轨道时间
        EOFdate = (re.sub("[-,:, ]", "", str(EOFdate)))[
            0:8
        ]  # 将时间格式转换成需要的数字格式,sub为去除字符串中符号
        return EOFdate


if __name__ == "__main__":
    print(
        SLCToDate.One(
            "S1A_IW_SLC__1SDV_20141003T235924_20141003T235951_002661_002F1D_1A1D.SAFE"
        )
        == str(20141003)
    )
    print(
        EOFToDate.One(
            "S1A_OPER_AUX_POEORB_OPOD_20231019T080710_V20230928T225942_20230930T005942.EOF"
        )
        == str(20230929)
    )
