# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 2:09 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : demo_move.py
# @Software: PyCharm


# 常用鼠标键盘操作
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# el = driver.find_element(By.NAME, "wd")
# # 1.对页面元素进行右击操作   ActionChains(driver).context_click(el).perform()
# ActionChains(driver).context_click(el).perform()
# # 2.双击   ActionChains(driver).double_click(el).perform()
# el = driver.find_element(By.ID, "su")
# driver.find_element(By.NAME, 'wd').send_keys("惆怅长岑长")
# time.sleep(2)
# ActionChains(driver).double_click(el).perform()

# 3.鼠标悬停
el = driver.find_element(By.ID,'s-usersetting-top')
ActionChains(driver).move_to_element(el).perform()
time.sleep(2)
driver.find_element(By.LINK_TEXT,'高级搜索').click()
time.sleep(1)
driver.quit()
