# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 9:47 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : demo_css04.py
# @Software: PyCharm


import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# css通过元素在页面布局的位置定位    一切皆为框
# 使用空格来做分隔符，遇到class就使用 . 遇到id就使用 #

# 1.使用绝对路径定位元素 定位百度首页新闻
# driver.find_element_by_css_selector(
#     'html body div#wrapper div#head div#s-top-left.s-top-left.s-isindex-wrap a+a').click()

# 2.通过相对路径定位
# driver.find_element_by_css_selector(
#     'div#s-top-left.s-top-left.s-isindex-wrap a+a').click()
# driver.find_element_by_css_selector('#kw').send_keys("测试")
# driver.find_element_by_css_selector('.s_ipt').send_keys("测试")

# 3.使用元素属性定位
# driver.find_element_by_css_selector('input[name="wd"][id="kw"]').send_keys("元素属性定位")

# 4.使用部分属性至匹配  https://www.hao123.com
# 4.1元素值开头包含内容：^=
# driver.find_element_by_css_selector('a[href^="https://www.hao123"]').click()
#
# # 4.2元素值结尾包含内容：$=
# driver.find_element_by_css_selector('a[href$="https://www.hao123]"').click()
#
# # 4.3元素值内容包含：*=
# driver.find_element_by_css_selector('a[href*="https://www.hao123"]').click()

# 5.查询子元素
# 5.1 查找第一子元素 first-child
# driver.find_element_by_css_selector('div#s-top-left a:first-child').click()

# 5.2 查找第n个子元素
# driver.find_element_by_css_selector('div#s-top-left a:nth-child(3)').click()
# driver.find_element_by_css_selector('div#s-top-left a:nth-child(6)').click()

# 6.查询兄弟元素 推荐使用5.2
driver.find_element_by_css_selector('div#s-top-left a+a+a+a').click()

time.sleep(2)

driver.quit()
