# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 8:45 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : demo_find_element03.py
# @Software: PyCharm

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

#  普通元素定位

# 1.通过id元素定位：
# driver.find_element_by_id('kw').send_keys("哈哈哈哈哈")
# 2.通过name元素定位：
# driver.find_element_by_name('wd').send_keys("新梦想IT教育")
# 3.通过class_name 定位输入框
# driver.find_element_by_class_name('s_ipt').send_keys("12306")
# 4.通过tag_name定位元素
# driver.find_element_by_class_name('s_ipt').send_keys("12306")
# driver.find_element_by_tag_name('form').submit()
# 5.通过link定位
# driver.find_element_by_link_text('hao123').click()
# 6.通过部分link定位
# driver.find_element_by_partial_link_text('123').click()

# driver.find_element_by_id('su').click()



time.sleep(2)

driver.quit()
