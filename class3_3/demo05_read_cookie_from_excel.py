# -*- coding: utf-8 -*-
# @Time : 2021/7/27 15:28
# @Author : Limusen
# @File : demo05_read_cookie_from_excel


import time
import xlrd
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.cnblogs.com/")
driver.implicitly_wait(10)
driver.maximize_window()

# 思路
# 1.打开excel表
book = r"C:\Users\admin\PycharmProjects\P9_P10selenium2\class3_3\Excel_cookies.xls"
work_book = xlrd.open_workbook(book)
# 2.读取sheet
sheet = work_book.sheet_by_name('cookie')
# 3.单行读取，存放到列表里面
cookie_list = []
for row_number in range(1, sheet.nrows):
    cookie_dict = {}
    cookie_dict['name'] = sheet.cell_value(row_number, 0)
    cookie_dict['value'] = sheet.cell_value(row_number, 1)
    cookie_dict['domain'] = sheet.cell_value(row_number, 2)
    cookie_dict['path'] = sheet.cell_value(row_number, 3)
    cookie_dict['httpOnly'] = bool(sheet.cell_value(row_number, 4))
    cookie_dict['secure'] = bool(sheet.cell_value(row_number, 5))
    cookie_list.append(cookie_dict)
print(cookie_list)
# 4.遍历列表
for cookie in cookie_list:
    driver.add_cookie(cookie)

# 5.加载所有cookie存入驱动
time.sleep(2)
driver.refresh()