# -*- coding: utf-8 -*-
# @Time : 2021/7/27 11:52
# @Author : Limusen
# @File : demo2_cookie02


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://47.107.178.45/zentao/www/index.php?m=user&f=login")
driver.implicitly_wait(10)

# 通过手动输入用户名密码，拿到登录后有效的cookie

# 1.先等待30秒，手动登录成功，再获取登录成功后的cookie

# 2.把所有拿到的cookie加载到driver，然后刷新页面
time.sleep(10)
cookies = driver.get_cookies()
for cookie in cookies:
    print(cookie)

# 　登录
# driver.find_element(By.XPATH,'//*[@id="account"]').send_keys('test01')
# driver.find_element(By.XPATH,'//*[@id="loginPanel"]/div/div[2]/form/table/tbody/tr[2]/td/input').send_keys("newdream123")
# driver.find_element(By.XPATH,'//*[@id="submit"]').click()


# time.sleep(2)
#
# driver.quit()
