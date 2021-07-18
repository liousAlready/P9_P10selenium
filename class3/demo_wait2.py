# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 3:10 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : demo_wait2.py
# @Software: PyCharm

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

STYLE = "background: blue; border: 2px solid red;"  # 高亮的样式


def highLightElement(driver, element):
    # 封装好的高亮显示页面元素的方法
    # 使用JavaScript代码将传入的页面元素对象的背景颜色和边框颜色分别
    # 设置为绿色和红色
    driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
                          element, "background:green ;border:2px solid red;")


# 1.扩展知识：元素高亮
driver = webdriver.Chrome()
driver.get("file:///Users/lishouwu/Downloads/Wait.html")

# 2.不加任何等待，直接报错

# driver.find_element(By.ID,'b').click()
# el = driver.find_element(By.CSS_SELECTOR, 'div.red_box')
# highLightElement(driver, el)

# 3.sleep()：固定休眠时间设置 固定等待7s

# driver.find_element(By.ID,'b').click()
# time.sleep(7)
# el = driver.find_element(By.CSS_SELECTOR, 'div.red_box')
# highLightElement(driver, el)

# 4.implicitlyWait()：隐式等待,  加隐式等待10秒

# driver.implicitly_wait(10)  # 只需要设置一次，整个代码都生效
# driver.find_element(By.ID, 'b').click()
# el = driver.find_element(By.CSS_SELECTOR, 'div.red_box')
# highLightElement(driver, el)

# 5.WebDriverWait():显示等待，加显示10s
driver.find_element(By.ID, 'b').click()
element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector('div.red_box'))

highLightElement(driver, element)

time.sleep(2)

driver.quit()
