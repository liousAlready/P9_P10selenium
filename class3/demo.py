# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 11:18 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : demo.py
# @Software: PyCharm


# 元素基本操作

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://47.107.178.45/zentao/www/index.php?m=user&f=loginz")
time.sleep(2)

# driver.find_element(By.NAME, "account").send_keys("tes12t")
# time.sleep(2)
# driver.find_element(By.NAME, "account").clear()
# time.sleep(2)
# driver.find_element(By.NAME, "account").send_keys("test")
# 元素和操作分离
element = driver.find_element(By.NAME, "account")
element.send_keys('test')
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("newdream123")
time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="submit"]').click()

size = element.size
print(size)

el2 = driver.find_element(By.XPATH, '//*[@id="loginPanel"]/div/div[2]/form/table/tbody/tr[4]/td[2]/a')
text = el2.text
print(text)

# get_attribute("属性名") : 获取对象的属性值
name = element.get_attribute('name')
id = element.get_attribute('id')
classname = element.get_attribute('classname')

print(name, id, classname)

# is_dispalyed() 用来判断对象是否可见
print("是否可见：", element.is_displayed())
print("是否被禁用：", element.is_enabled())

# is_selected(): 判断对象是否被选中
el3 = driver.find_element(By.NAME, 'keepLogin[]')
print('是否被选中：', el3.is_selected())

# tag_name: 获取对象标签名称
print("标签名: ", element.tag_name)

# location 获取坐标
print("获取坐标：", element.location)

time.sleep(2)
driver.quit()
