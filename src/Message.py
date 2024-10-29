#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    :2024/10/29 23:29:08
# @Author  :小 y 同 学
# @公众号   :小y只会写bug
# @CSDN    :https://blog.csdn.net/weixin_64989228?type=blog
# @Discript:字符串消息


class Message:
    def __init__(self):
        pass

    # region 与终端交互
    @staticmethod
    def print_help():
        print("Usage: python3 main.py [options] [args]")
        print("Options:")
        print("  -h, --help")

    # endregion

    # region 建立字符串，可连接界面
    @staticmethod
    def str_help():
        str = "Usage: python3 main.py [options] [args]\n"
        str += "Options:\n"
        str += "  -h, --help\n"

    # endregion
