# -*- coding: utf-8 -*-
# @Time    : 2021/7/14 9:22 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : demo1.py
# @Software: PyCharm
import time

from selenium import webdriver

# 浏览器操作
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(2)
driver.maximize_window()
time.sleep(1)
driver.minimize_window()
time.sleep(1)
driver.set_window_size(200, 200)
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)

url = driver.current_url
print(url)

title = driver.title
print(title)

page = driver.page_source
print(page)

driver.get_screenshot_as_file('..' + '/file/baidu.png')

driver.quit()
