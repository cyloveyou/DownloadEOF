#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    :2024/10/29 23:28:48
# @Author  :小 y 同 学
# @公众号   :小y只会写bug
# @CSDN    :https://blog.csdn.net/weixin_64989228?type=blog
# @Discript:命令行交互

import sys
from src.Message import Message

argv = sys.argv
if len(argv) == 1:
    Message.print_help()
    sys.exit(0)
elif argv[1] == "-h" or argv[1] == "--help":
    Message.print_help()
    sys.exit(0)
else:
    pass
