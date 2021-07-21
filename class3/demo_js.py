# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 5:02 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : demo_js.py
# @Software: PyCharm


# 弹出提示框
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///Users/lishouwu/Downloads/alert.html")

driver.find_element_by_id("alert").click()

# 1.alert 只能确实返回结果
# 1.1 accept : 点击确认按钮
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
time.sleep(2)
# text 返回alert/config/prompt 的文字内容

# 2.confirm 可以确认，可以取消
driver.find_element_by_id('confirm').click()
time.sleep(2)
driver.switch_to.alert.dismiss()

# 3.prompt 可以输入内容
driver.find_element_by_id("prompt").click()
driver.switch_to.alert.send_keys("新梦想")

time.sleep(2)

driver.quit()
