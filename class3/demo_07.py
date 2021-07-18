# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 3:58 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : demo_07.py
# @Software: PyCharm


# 定位一组元素

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(10)

el = driver.find_element(By.ID, "s-usersetting-top")
ActionChains(driver).move_to_element(el).perform()

driver.find_element(By.PARTIAL_LINK_TEXT, '高级搜索').click()

redio_list = driver.find_elements(By.NAME, 'q5')
# 先选择一个
redio_list[1].click()

# 循环遍历
time.sleep(2)
for i in redio_list:
    i.click()
    time.sleep(2)

# 循环遍历输入
inputs = driver.find_elements_by_css_selector("input.c-input.adv-q-input")
for send in inputs:
    send.send_keys("sssxxx")
    time.sleep(0.5)

time.sleep(2)

driver.quit()
