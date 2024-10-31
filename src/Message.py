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
        content = ""
        content += "This is a tool to download Sentinel-1 orbit data from ASF.\n\n"
        content += "Usage: SentinelOrbit.py [options]"
        content += "Options:\n"
        content += "  -c, --config  Create a default configuration file in the current working directory\n"
        content += "  -d, --default Use the default(in user home) configuration file in the current working directory\n"
        content += "  xx.ini,       Use the specified configuration file\n"
        content += "  -h, --help    Print this page\n"
        content += "  -v, --version Print current version\n"
        content += "\n"
        content += (
            "Welcome to star the github: https://github.com/cyloveyou/SentinelOrbit \n"
        )
        content += (
            "I'd appreciate it if you could give me some suggestions and ideas.\n"
        )

        return content

    @addDate
    def str_info(msg: str = "*" * 50) -> str:
        """一般提示"""
        content = f"[Info]:{msg}"
        return content

    @addDate
    def str_error(msg: str) -> str:
        """错误提示"""
        content = f"[Error]:{msg}"
        return content

    @addDate
    def str_exist(filePath: str) -> str:
        """已经存在文件提示"""
        content = f"[Exist&Skip]:{filePath}"
        return content

    @addDate
    def str_downloading(
        eoflink: str,
    ) -> str:
        """正在下载提示"""
        content = f"[Downloading]:{eoflink}"
        return content

    @addDate
    def str_downloadOK(filePath: str) -> str:
        """下载成功提示"""
        content = f"[DownloadOK]:{filePath}"
        return content

    # endregion


if __name__ == "__main__":
    print(Message.str_help())
    print(Message.str_info("test"))
    time.sleep(1)
    print(Message.str_error("test"))
    print(Message.str_exist("test"))
    print(Message.str_downloading("test"))
    print(Message.str_downloadOK("test"))
