#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    :2024/10/29 19:13:49
# @Author  :小 y 同 学
# @公众号   :小y只会写bug
# @CSDN    :https://blog.csdn.net/weixin_64989228?type=blog
# @Discript:下载数据
import os
import requests
from Message import *
from concurrent.futures import ThreadPoolExecutor


def DownloadOne(eoflink, cookie, saveFolder=".", proxies=None):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": cookie,
        "Host": "s1qc.asf.alaska.edu",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows "',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    }
    if not os.path.exists(saveFolder):
        os.makedirs(saveFolder)

    filePath = os.path.join(saveFolder, eoflink.split("/")[-1])
    tempPath = filePath + ".temp"
    try:
        with requests.get(
            url=eoflink, headers=headers, stream=True, proxies=proxies, timeout=10
        ) as res:
            content_length = int(res.headers.get("Content-Length", 0))
            if res.status_code == 200:
                downloaded_size = 0
                with open(tempPath, "wb") as f:
                    for chunk in res.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            downloaded_size += len(chunk)
                if downloaded_size == content_length:
                    os.rename(tempPath, filePath)
                else:
                    return False
                return True
            else:
                return False
    except Exception as e:
        return False


def DownloadSingle(eoflink, cookie, saveFolder=".", proxies=None):
    """单个下载"""
    filePath = os.path.join(saveFolder, eoflink.split("/")[-1])
    if os.path.exists(filePath):
        Message.print_exist(filePath)
        return True
    Message.print_downloading(eoflink)
    flag = DownloadOne(eoflink, cookie, saveFolder, proxies)
    while not flag:
        Message.print_error(f"{eoflink} Download failed, retrying...")
        time.sleep(1)
        flag = DownloadOne(eoflink, cookie, saveFolder, proxies)
    Message.print_downloadOK(eoflink)
    return False


def DownloadMulit(eoflinks, cookie, workers=3, saveFolder=".", proxies=None):
    """多进程下载"""
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for eoflink in eoflinks:
            executor.submit(DownloadSingle, eoflink, cookie, saveFolder, proxies)
    return True


if __name__ == "__main__":
    pass
