#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    :2024/10/29 23:29:08
# @Author  :小 y 同 学
# @公众号   :小y只会写bug
# @CSDN    :https://blog.csdn.net/weixin_64989228?type=blog
# @Discript:字符串消息
from datetime import datetime
import time


def addDate(func):  # 日期装饰器
    def wrapper(*args, **kwargs):
        now = datetime.now()
        format_now = now.strftime("[%Y-%m-%d %H:%M:%S]")
        result = f"{format_now} {func(*args, **kwargs)}"
        return result

    return wrapper


class Message:
    def __init__(self):
        pass

    # region 与终端交互
    def print_help():
        print(Message.str_help())

    def print_info(msg: str):
        print(Message.str_info(msg))

    def print_error(msg: str):
        print(Message.str_error(msg))

    def print_exist(filePath: str):
        print(Message.str_exist(filePath))

    def print_downloading(eoflink: str):
        print(Message.str_downloading(eoflink))

    def print_downloadOK(filePath: str):
        print(Message.str_downloadOK(filePath))

    # endregion

    # region 建立字符串，可连接界面
    def str_help() -> str:
        """帮助文档"""
        str = "Usage: python3 main.py [options] [args]\n"
        str += "Options:\n"
        str += "  -h, --help\n"
        return str

    @addDate
    def str_info(msg: str = "*" * 50) -> str:
        """一般提示"""
        str = f"[Info]:{msg}"
        return str

    @addDate
    def str_error(msg: str) -> str:
        """错误提示"""
        str = f"[Error]:{msg}"
        return str

    @addDate
    def str_exist(filePath: str) -> str:
        """已经存在文件提示"""
        str = f"[Exist&Skip]:{filePath}"
        return str

    @addDate
    def str_downloading(
        eoflink: str,
    ) -> str:
        """正在下载提示"""
        str = f"[Downloading]:{eoflink}"
        return str

    @addDate
    def str_downloadOK(filePath: str) -> str:
        """下载成功提示"""
        str = f"[DownloadOK]:{filePath}"
        return str

    # endregion


if __name__ == "__main__":
    print(Message.str_help())
    print(Message.str_info("test"))
    time.sleep(1)
    print(Message.str_error("test"))
    print(Message.str_exist("test"))
    print(Message.str_downloading("test"))
    print(Message.str_downloadOK("test"))
