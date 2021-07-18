# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 9:09 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : demo_xpath04.1.py
# @Software: PyCharm


import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# xpath定位方式

# 1.通过绝对路径定位  定位百度页面的 hao123
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/a[2]').click()

# 2.通过相对路径定位 使用 // 标识相对路径
# xpath相对路径是从后向前取值，如果取不到值就多提取一个上级标签，让其保持唯一性
# driver.find_element_by_xpath('//div[3]/a[2]').click()
# driver.find_element_by_xpath('//div[1]/div[3]/a[2]').click()

# 3.使用元素属性进行定位
# 3.1 单属性 识别百度输入框
# driver.find_element_by_xpath('//input[@id="kw"]').send_keys("通过属性识别")
# driver.find_element_by_xpath('//input[@class="s_ipt"]').send_keys("通过属性识别")

# 3.2 多属性  通过一个节点多个元素值定位
# driver.find_element_by_xpath('//input[@id="kw" and @class="s_ipt"]').send_keys("多属性识别")

# 4.动态元素的识别   http://news.baidu.com
# 4.1 元素属性开头的内容： starts-with()
# driver.find_element_by_xpath('//a[starts-with(@href,"http://news")]').click()
# 421 元素属性结尾包含的内容： substring()  https://www.hao123.com  substring(@href)=""
# driver.find_element_by_xpath('//a[substring(@href,13)="hao123.com"]').click()  # 13 从第13个元素开始取
# 4.1 元素属性中间包含的内容： contains()
# driver.find_element_by_xpath('//a[contains(@href,"hao123")]').click()

# 5.元素文本在xpath中可以通过text() 函数
driver.find_element_by_xpath('//a[text()="新闻"]').click()

time.sleep(2)

driver.quit()
