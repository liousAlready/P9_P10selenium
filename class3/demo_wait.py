# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 2:55 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : demo_wait.py
# @Software: PyCharm


# 等待操作

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

STYLE = "background: green; border: 2px solid red;"  # 高亮的样式


def find(driver, by, expr):
    element = driver.find_element(by, expr)
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, STYLE)
    return element


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
find(driver,By.NAME,'wd').click()
# 实验步骤：

# 1.扩展知识：元素高亮

# 2.不加任何等待，直接报错

# 3.sleep()：固定休眠时间设置 固定等待7s

# 4.implicitlyWait()：隐式等待,  加隐式等待10秒

# 5.WebDriverWait():显示等待，加显示10s
