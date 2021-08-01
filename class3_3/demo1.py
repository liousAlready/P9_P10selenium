# -*- coding: utf-8 -*-
# @Time : 2021/7/27 10:26
# @Author : Limusen
# @File : demo1


# 　多窗口处理　句柄

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.implicitly_wait(10)

time.sleep(2)

# 获取百度的句柄
now_handels = driver.current_window_handle
print(now_handels)

# 获取所有句柄
driver.find_element_by_xpath('//*[@id="bottom_layer"]/div/p[5]/a').click()
time.sleep(1)

all_handels = driver.window_handles
print(all_handels)
# 切换句柄
driver.switch_to.window(all_handels[1])
driver.find_element_by_xpath('//*[@id="record"]').send_keys("哈哈哈")
time.sleep(2)
# driver.close()

driver.switch_to.window(now_handels)

driver.find_element_by_name('wd').send_keys("哈哈哈sssss")
