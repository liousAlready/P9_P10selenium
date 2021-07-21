# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 8:28 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : demo_js.py
# @Software: PyCharm


# 执行js脚本

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.implicitly_wait(10)

# # 执行js脚本
# driver.execute_script("alert('shabi');")

# wl = driver.find_element_by_name('wd')
# driver.execute_script("arguments[0].style.border='5px solid red'", wl)  # 加边框

# #  获取元素的属性
# js = "var user_input= document.getElementById('su').getAttribute('id'); return user_input;"
# driver.execute_script(js)
#
# id = driver.execute_script('return document.getElementById("su").getAttribute("id");')
# value = driver.execute_script('return document.getElementById("su").getAttribute("value");')
# class_name = driver.execute_script('return document.getElementById("su").getAttribute("class");')
# name = driver.execute_script('return document.getElementById("kw").getAttribute("name");')
#
# print(id)
# print(value)
# print(class_name)
# print(name)

#  滚动条操作，封装成函数
#
# driver.find_element_by_name("wd").send_keys("新梦想")
# time.sleep(2)
# driver.find_element_by_id("su").click()
# time.sleep(1)

# js = "window.scrollBy(0,500)"
# driver.execute_script(js)
# time.sleep(2)
# js = "window.scrollBy(0,500)"
# driver.execute_script(js)
#
# js = "window.scrollBy(0,-1000)"
# driver.execute_script(js)

# def scoll(driver, heigh):
#     time.sleep(2)
#     js = "window.scrollBy(0," + str(heigh) + ")"
#     driver.execute_script(js)
#
#
# scoll(driver, 500)
# time.sleep(2)
# scoll(driver, 1000)

#  改元素的属性

# el = driver.find_element_by_name("wd")
# js = 'arguments[0].removeAttribute("id")'
# driver.execute_script(js,el)

js = 'arguments[0].setAttribute("value","newdream")'
driver.execute_script(js)


time.sleep(2)
# driver.quit()
