# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 8:11 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : demo_xialakuang.py
# @Software: PyCharm

import time
from selenium import webdriver
import executing
from selenium.webdriver.support.select import Select

# 下拉框的处理

driver = webdriver.Chrome()
driver.get("file:///Users/lishouwu/Downloads/select.html")
driver.maximize_window()
driver.implicitly_wait(10)

# 方法一： 直接定位元素
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="status"]/option[3]').click()

# 方法二: 层级定位
# driver.find_element_by_id("status").find_element_by_xpath('//*[@id="status"]/option[3]').click()

# 方法三：使用select对象
select_element = driver.find_element_by_id('status')

# 3.1  通过index索引位置
# s = Select(select_element)
# s.select_by_index(1)

# 3.2  通过value值
# s = Select(select_element)
# s.select_by_value("3")

# 3.3 通过文本信息
# s = Select(select_element)
# s.select_by_visible_text("审核不通过")


time.sleep(2)

driver.quit()