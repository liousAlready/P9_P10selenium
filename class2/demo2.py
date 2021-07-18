# -*- coding: utf-8 -*-
# @Time    : 2021/7/15 10:25 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : demo2.py
# @Software: PyCharm
import time
from icecream import ic
from selenium import webdriver

# driver = input("输入你想要的运行的浏览器：")
# while True:
#     if driver == "chrome":
#         ic("当前正在启动: %s" % driver)
#         driver = webdriver.Chrome()
#     elif driver == 'firefox':
#         ic("当前正在启动: %s" % driver)
#         driver = webdriver.Firefox()
#     else:
#         ic("当前暂不支持此浏览器")
#         break
#
#     driver.get("http://www.hnxmxit.com")
#     time.sleep(2)
#     driver.quit()

from selenium import webdriver

driver = webdriver.Chrome()  # 将chrome() 驱动定义成一个变量driver
driver.get("https://www.baidu.com")  # 打开浏览器
driver.minimize_window()  # 将浏览器最小化
driver.maximize_window()  # 将浏览器最大化
driver.find_element_by_id("kw").send_keys("测试我们的代码")  # find_element_by_id,定位到的元素中有id的标识，我们可以直接引用
driver.find_element_by_id("su").click()  # 点击我们定位到的元素
driver.get_screenshot_as_file('..' + '/file/baidutest.png')  # 截图并将文件存放在根目录下的file文件中
driver.quit()  # 退出浏览器，避免消耗太多内存

import unittest