# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 2:32 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : demo_jianpan.py
# @Software: PyCharm

# 键盘操作

# 常用鼠标键盘操作
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# # 1.单键操作
# driver.find_element(By.ID, 'su').click()
# # 切换tab键
# driver.find_element(By.ID, 'su').send_keys(Keys.TAB)

# # 回退键
# driver.find_element(By.NAME, 'wd').send_keys("我丢雷母")
# time.sleep(1)
# driver.find_element(By.ID, 'su').click()
#
# for i in range(1, 6):
#     driver.find_element(By.NAME, 'wd').send_keys(Keys.BACK_SPACE)
#     time.sleep(1)


# 2.组合键
# 方法一：普通操作
driver.find_element(By.ID, 'kw').click()
# driver.find_element(By.ID,'kw').send_keys(Keys.COMMAND,'v')

# 方法二：组合方法  必须先按下，然后在抬起来   key_down  ==》 key_up
ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

time.sleep(2)
driver.quit()
