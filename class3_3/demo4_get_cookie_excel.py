# -*- coding: utf-8 -*-
# @Time : 2021/7/27 14:59
# @Author : Limusen
# @File : demo4_get_cookie_excel


import time
import xlwt
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.cnblogs.com/")
driver.implicitly_wait(10)

# 新建一个excel 请准备好表头
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('cookie')

# 准备表头
worksheet.write(0, 0, 'name')
worksheet.write(0, 1, 'value')
worksheet.write(0, 2, 'domain')
worksheet.write(0, 3, 'path')
worksheet.write(0, 4, 'httpOnly')
worksheet.write(0, 5, 'secure')

time.sleep(20)
cookies = driver.get_cookies()
print(cookies)

for i in range(1, len(cookies) + 1):  # 取8行 包前不包后
    worksheet.write(i, 0, cookies[i - 1]['name'])
    worksheet.write(i, 1, cookies[i - 1]['value'])
    worksheet.write(i, 2, cookies[i - 1]['domain'])
    worksheet.write(i, 3, cookies[i - 1]['path'])
    worksheet.write(i, 4, cookies[i - 1]['httpOnly'])
    worksheet.write(i, 5, cookies[i - 1]['secure'])

# 保存
workbook.save('Excel_cookies.xls')
print("Cookies已保存")
