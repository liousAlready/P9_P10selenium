# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 4:13 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : demo_08.py
# @Software: PyCharm


# 层级定位

import time
import os
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(10)

driver.find_element_by_id("s-top-loginbtn").click()

driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()

driver.find_element_by_id("TANGRAM__PSP_11__form").find_element_by_id("TANGRAM__PSP_11__userName").send_keys(
    "15574933885")
time.sleep(1)
driver.find_element_by_id("TANGRAM__PSP_11__form").find_element_by_id("TANGRAM__PSP_11__password").send_keys(
    "15574933885")

time.sleep(2)

driver.quit()
