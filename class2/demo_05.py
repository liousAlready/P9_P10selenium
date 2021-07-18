# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 10:51 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : demo_05.py
# @Software: PyCharm

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 识别元素进阶
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 将识别方法与识别属性分离开
# driver.find_element(By.NAME, 'wd').send_keys("擦")
# driver.find_element(By.CLASS_NAME,'s_ipt').send_keys("元素识别方法")
# driver.find_element(By.ID,'su').click()
# driver.find_element(By.PARTIAL_LINK_TEXT, 'hao').click()
# driver.find_element(By.CSS_SELECTOR,'#kw').send_keys("12306")

time.sleep(2)
driver.quit()
