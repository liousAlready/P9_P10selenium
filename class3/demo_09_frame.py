# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 4:27 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : demo_09_frame.py
# @Software: PyCharm


# 框架

import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("file:///Users/lishouwu/Downloads/frame/frame/frame.html")
driver.implicitly_wait(5)

# # 有id或者name
# driver.switch_to.frame('top')
# driver.find_element_by_name("message").send_keys("selenium自动化测试")
# time.sleep(2)
#
# # 回到整体框架
# driver.switch_to.default_content()
#
# # 切换到左框架
# driver.switch_to.frame('left')
# driver.find_element_by_name("message").send_keys("selenium自动化测试002")
# driver.switch_to.default_content()
# time.sleep(2)
#
# # 切换到主框架
# driver.switch_to.frame("main")
# driver.find_element_by_name("message").send_keys("hahahahah")
# driver.switch_to.default_content()


# 没有ID或者Name的处理
# 1.通过xpath
driver.switch_to.frame("框架的xpath")
# 2.把框架做成一个元素
framle = driver.find_element_by_xpath("")
driver.switch_to.frame(framle)

time.sleep(2)
driver.quit()
