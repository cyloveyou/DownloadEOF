#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    :2024/10/29 23:28:48
# @Author  :小 y 同 学
# @公众号   :小y只会写bug
# @CSDN    :https://blog.csdn.net/weixin_64989228?type=blog
# @Discript:命令行交互

import sys
import os

from src.Message import *
from src.Cookie import *
from src.SentinelOrbit import *
from src.InputParam import *
from src.SetConfig import *
from src.ExtractDate import *
from src.ExtractSLC import *
from src.Download import *
from src.FindOrbit import *


def main(configfile):
    # 1.读取配置文件
    Message.print_info(f"1. Read config file from {configfile}...")
    param = inputParam(configfile)
    if param.ipport:
        proxies = {"http": param.ipport, "https": param.ipport}
    else:
        proxies = None
    Message.print_info(f"Read config file OK.")

    # 2.获取SLC文件列表
    if os.path.isdir(param.inputslc):
        Message.print_info(f"2. Find SLC from {param.inputslc}")
        SLClist = ExtractDate.from_slc_folder(param.inputslc)
    elif param.inputslc.endswith(".py"):
        Message.print_info(f"2. Find SLC from {param.inputslc}")
        SLClist = ExtractDate.form_asf_pylink(param.inputslc)
    elif param.inputslc.endswith(".metalink"):
        Message.print_info(f"2. Find SLC from {param.inputslc}")
        SLClist = ExtractDate.from_asf_metlink(param.inputslc)
    else:
        Message.print_error(
            f"Can't understand the config inputslc, the value is {param.inputslc}. Please check the config file."
        )
        sys.exit(0)
    Message.print_info(f"Find {len(SLClist)} SLC files.")
    if len(SLClist) == 0:
        sys.exit(0)

    # 3.获取轨道文件列表
    Message.print_info("3. Get orbit file list...")
    findorb = FindOrbit(proxies)
    orbitList = findorb.fromSLCList(SLClist)
    Message.print_info(f"Get {len(orbitList)} orbit files.")

    # 4.获取cookie
    Message.print_info("4. Get cookie...")
    cookie = Cookie(param.userid, param.userpwd).getCookie(proxies)
    Message.print_info("Get cookie OK.")

    # 5.下载轨道文件
    Message.print_info(f"5. Download orbit files, savepath={param.savepath}")
    DownloadMulit(
        orbitList,
        cookie,
        workers=param.workers,
        saveFolder=param.savepath,
        proxies=proxies,
    )
    Message.print_info("Download orbit files OK.")


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 1:
        Message.print_help()
        sys.exit(0)
    elif argv[1] == "-c":
        SetConfig.CreatDefault()
        sys.exit(0)
    elif argv[1] == "-h" or argv[1] == "--help":
        Message.print_help()
        sys.exit(0)
    elif argv[1] == "-v" or argv[1] == "--version":
        print("version 1.0")
    elif argv[1].endswith(".ini"):
        main(argv[1])
    else:
        print("Please enter the correct parameters")
        Message.print_help()
        sys.exit(0)
