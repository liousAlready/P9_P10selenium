# -*- coding: utf-8 -*-
# @Time : 2021/7/27 11:18
# @Author : Limusen
# @File : demo2_cookies


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://47.107.178.45/zentao/www/index.php?m=user&f=login")
driver.implicitly_wait(10)

# 　登录
# driver.find_element(By.XPATH,'//*[@id="account"]').send_keys('test01')
# driver.find_element(By.XPATH,'//*[@id="loginPanel"]/div/div[2]/form/table/tbody/tr[2]/td/input').send_keys("newdream123")
# driver.find_element(By.XPATH,'//*[@id="submit"]').click()


time.sleep(2)

# # 　1.获取所有的cookie
# cookies = driver.get_cookies()
# for cookie in cookies:
#     print(cookie)
# print("------------------------------------------------")

# #   2.获取单个cookie值 get_cookie(name)
# zentao_sid_cookie = driver.get_cookie('zentaosid')
# print(zentao_sid_cookie)

# # 3.手动获取cookie
# cookie = {'name': 'zentaosid', 'domain': '47.107.178.45', 'value': 'd96ceh9413imssjdjn8gt0gav4',
#           'path': "/"}
#
# driver.add_cookie(cookie)  # 把cookie加载到驱动
# driver.refresh()  # 刷新页面，让cookie生效



time.sleep(4)

driver.quit()
