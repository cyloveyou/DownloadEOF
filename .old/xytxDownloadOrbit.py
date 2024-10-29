# -*- coding: utf-8 -*-
# @Time    :2024/8/2 9:58
# @Author  :小 y 同 学
# @公众号   :小y只会写bug
# @CSDN    :https://blog.csdn.net/weixin_64989228?type=blog

import datetime
import os
import re
import shutil
import urllib.request
from urllib.parse import urlparse

import requests
from dateutil.parser import parse


# https: // s1qc.asf.alaska.edu / aux_poeorb / S1B_OPER_AUX_POEORB_OPOD_20210317T183415_V20200325T225942_20200327T005942.EOF


class MyFile:
	def __init__(self, SLC):
		self.SLC = SLC
		self.sentinel = ""
		self.SLCdate = ""
		self.EOF = ""

		self.GetInfoFromSLC()

	def GetInfoFromSLC(self):
		temp = re.findall('_(\d{8})T', self.SLC)
		self.sentinel = self.SLC.split('/')[-1][0:3]
		self.SLCdate = temp[0]  # 起始时间

	def FindOrbit(self, EOFList):
		date = parse(self.SLCdate) + datetime.timedelta(days=-1)
		date = (re.sub('[-,:, ]', '', str(date)))[0:8]  # 将时间格式转换成需要的数字格式,sub为去除字符串中符号

		for eof in EOFList:
			if os.path.splitext(eof)[1] == ".EOF" and os.path.basename(eof)[0:3] == self.sentinel:  # 后缀是eof且前缀前三个字符为S1A
				SplitTime = re.findall("V(\d+)T", eof)[0]
				if SplitTime == date:
					self.EOF = f"https://s1qc.asf.alaska.edu/aux_poeorb/{eof}"
					return

	def download(self, saveFolder, cookiePath, proxies=None):

		cookie = str(open(cookiePath, "r").read())
		headers = {
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"Accept-Encoding": "gzip, deflate, br",
			"Accept-Language": "zh-CN,zh;q=0.9",
			"Connection": "keep-alive",
			"Cookie": cookie,
			"Host": "s1qc.asf.alaska.edu",
			"Referer": "https://s1qc.asf.alaska.edu/aux_poeorb/?sentinel1__mission=S1A&validity_start=2015-02-19",
			"sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
			"sec-ch-ua-mobile": "?0",
			"sec-ch-ua-platform": "\"Windows \"",
			"Sec-Fetch-Dest": "document",
			"Sec-Fetch-Mode": "navigate",
			"Sec-Fetch-Site": "same-origin",
			"Sec-Fetch-User": "?1",
			"Upgrade-Insecure-Requests": "1",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
		}

		filePath = os.path.join(saveFolder, self.EOF.split('/')[-1])
		tempPath = filePath + ".temp"

		# 对已有的文件不破坏
		if os.path.exists(filePath):
			print("已经存在---{filePath}---跳过下载")
			return
		try:
			print(f"保存文件：{self.EOF}")

			response = requests.get(url=self.EOF, headers=headers, proxies=proxies)
			while response.status_code != 200:
				print(f"下载失败，重新下载：{self.EOF}")
				print()
				response = requests.get(url=self.EOF, headers=headers, proxies=proxies)
			f = open(tempPath, "w")
			f.write(response.text)
			f.close()

			shutil.move(tempPath, filePath)
			print(f"保存成功！：{filePath}")
		except:
			print("保存失败！：{filePath}---尝试重新下载")
			self.download(saveFolder, cookiePath, proxies)


def CreatEOF(sentinel1__mission='S1A', validity_start='2019-01-01'):
	# 获得EOF下载网址
	url_param_json = {}
	url_param_json['sentinel1__mission'] = sentinel1__mission
	url_param_json['validity_start'] = date

	url_param = urllib.parse.urlencode(url_param_json)  # url参数
	url = 'https://s1qc.asf.alaska.edu/aux_poeorb/?%s' % url_param  # 拼接

	return url


def ExtractDateFromPY(pyPath):
	"""从PY文件中提取日期"""
	with open(pyPath, 'r', encoding="utf-8") as f:
		data = f.read()
		slc = re.findall('(https:.*.zip)', data)
	fileList = []
	for i in slc:
		file = MyFile(i)
		fileList.append(file)
	return fileList


if __name__ == '__main__':
	cookie_path = r'cookie.txt'  # todo cookie文件位置

	SavePath = "./test"  # todo 设置保存EOF文件的文件夹
	date = '2024-01-01'  # 开始搜寻日期，可以不用管

	IPPort = "127.0.0.1:43654"  # todo 设置代理

	PY = "download-all-2024-07-31_10-18-25.py"  # todo ASF官网下载的python脚本，用于提取SCL中的日期

	proxies = {
		"http": IPPort,
		"https": IPPort
	}

	# 1.创建保存路径文件夹
	os.path.exists(SavePath) or os.makedirs(SavePath)

	# 2.从slc的下载链接中提取Date

	fileList = ExtractDateFromPY(PY)

	# 3.搜寻轨道数据
	print("查找所有轨道数据".center(50, "*"))
	EOF = CreatEOF()
	# print(EOF)  # 打印EOF网址
	res = requests.get(EOF,
	                   proxies=proxies).text
	orbitList = re.findall('href="(.*?\.EOF)">', res)
	# print(orbitList)  # 打印所有轨道数据

	print("寻找轨道数据".center(50, "*"))
	for file in fileList:
		file.FindOrbit(orbitList)
	for file in fileList:
		file.download(SavePath, cookie_path, proxies=proxies)
