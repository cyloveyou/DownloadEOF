#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    :2024/10/30 00:13:47
# @Author  :小 y 同 学
# @公众号   :小y只会写bug
# @CSDN    :https://blog.csdn.net/weixin_64989228?type=blog
# @Discript:生成配置文件


from configparser import ConfigParser
import os


class SetConfig:
    def __init__(self) -> None:
        pass

    def CreatDefault() -> None:
        conf = ConfigParser()
        # ASF相关信息
        conf.add_section("ASFInfo")
        conf.set("ASFInfo", "userid", "xxxxxx")
        conf.set("ASFInfo", "userpwd", "xxxxxx")

        # SLC相关
        conf.add_section("SLCInfo")
        conf.set("SLCInfo", "inputslc", ".")

        # 轨道相关
        conf.add_section("OrbitInfo")
        conf.set("OrbitInfo", "savepath", ".")

        # 代理相关
        conf.add_section("OtherInfo")
        conf.set("OtherInfo", "ipport", "")
        conf.set("OtherInfo", "workers", "")

        conf.write(open("config.ini", "w"))
