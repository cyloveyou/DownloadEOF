#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    :2024/10/30 13:47:17
# @Author  :小 y 同 学
# @公众号   :小y只会写bug
# @CSDN    :https://blog.csdn.net/weixin_64989228?type=blog
# @Discript:根据账号密码获取登录cookie
import requests
from src.Message import *


class Cookie:
    def __init__(self, userId: str, userPwd: str) -> None:
        """_summary_

        Args:
            userId (str): ASF账号
            userPwd (str): ASF密码
        """
        self.userId = userId
        self.userPwd = userPwd

    def getCookie(self, proxies=None) -> str:
        """获取下载ASF数据所需要的cookie

        Returns:
            _type_: _description_
        """
        url = (
            "https://urs.earthdata.nasa.gov/oauth/authorize?response_type=code&"
            "client_id=BO_n7nTIlMljdvU6kRRB3g&redirect_uri=https://auth.asf.alaska.edu/login&"
        )
        headers = {
            "response_type": "code",
            "client_id": "BO_n7nTIlMljdvU6kRRB3g",
            "redirect_uri": "https://auth.asf.alaska.edu/login",
        }
        login_data = {
            "username": self.userId,
            "password": self.userPwd,
        }
        try:
            with requests.session() as s:
                res = s.get(url, auth=(self.userId, self.userPwd), proxies=proxies)
                if res.status_code == 200:
                    cookie_dict = requests.utils.dict_from_cookiejar(s.cookies)
                    return f"asf-urs={cookie_dict['asf-urs']}"
        except Exception as e:
            Message.print_error(
                f"{str(e)}\nAn exception occurred while getting the cookie, retrying..."
            )
            time.sleep(1)
            self.getCookie(proxies)


if __name__ == "__main__":
    # userId = ""
    # userPwd = ""
    # cookie = Cookie(userId, userPwd)
    # print(cookie.getCookie())
    # IPPort = "127.0.0.1:10086"
    # proxies = {"http": IPPort, "https": IPPort}
    # print(cookie.getCookie(proxies))
    pass
