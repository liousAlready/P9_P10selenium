# -*- coding: utf-8 -*-
# @Time : 2021/7/27 14:18
# @Author : Limusen
# @File : demo4_get_cookie

import time
import xlwt
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.cnblogs.com/")
driver.implicitly_wait(10)

# # 获取cookie
# time.sleep(10)
# cookies = driver.get_cookies()
# for cookie in cookies:
#     print(cookie)

time.sleep(2)

driver.add_cookie({'domain': '.cnblogs.com', 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
                   'value': 'GA1.2.18250488.1627368344'})
driver.add_cookie(
    {'domain': 'www.cnblogs.com', 'httpOnly': True, 'name': '.AspNetCore.Antiforgery.b8-pDmTq1XM', 'path': '/',
     'secure': False,
     'value': 'CfDJ8NACB8VE9qlHm6Ujjqxvg5BvLHZDc-PS8dwtA3-VWazEfjjnLdoJZrDJptmmxSUQfFuq2zsJyUGdAxhutceJULKVIPlVCB6cbJZ_QYOghSr1oBIvmwJExptjRfJDS5W5Z3LzCHllVK0VFutKxHboRMU'}
    )
driver.add_cookie({'domain': '.cnblogs.com', 'httpOnly': False, 'name': '_ga_3Q0DVSGN10', 'path': '/', 'secure': False,
                   'value': 'GS1.1.1627368346.1.1.1627368356.50'}
                  )
driver.add_cookie({'domain': '.cnblogs.com', 'httpOnly': True, 'name': '.CNBlogsCookie', 'path': '/', 'secure': False,
                   'value': '0B6FCD14E42C12F42343B95C1436681F45C5C2DDA9F3557A8DE24138F813DEE6C5561BCA9B1D9D1EBF376C6A6F62CCECDBFEA199C82822F1D22782A84FFA72D0FF0D9ED09FED20B9DF9C11FD0FB75653B102911D'}
                  )
driver.add_cookie(
    {'domain': '.cnblogs.com', 'httpOnly': True, 'name': '.Cnblogs.AspNetCore.Cookies', 'path': '/', 'secure': False,
     'value': 'CfDJ8NACB8VE9qlHm6Ujjqxvg5Dtxc6DhIs3vlLHhZKoEfZpG62BFHFgnmnnWnqWKKk-q3JaRxrNFnL1dIMBAcpMdkxBud6ox_aLLjiuEw0et6gemFZ_BmqUKH_-AILV7PLSOwMrO1_6WG8M7XDj4hSXxgW5Q8zmOU20aAj__RSe_BTEd1d3Ajh_zWrfM4WH91gKgmOZpz5LbHUjG0NktBlWecbTtfwUoUeBuyVSRYz7Nie3tymxNea6JvkPkLY9J_m5mUO7Q5zznjOeEEzMeYIaH4moYWC-gsxPFC3MQ3K9GPW_c8iTOfAhOn7bb4rkgDbZc-9sUv-gyfmbxsg7YmbIKsoVY8tgNFWabYo0Uq0ApxaWWfQs-VzfNAbROOi_pMc8NwhH9oHzb_-Mwmo6UGCfRda_ur-uRp3nqVf9Y6r0vgwBBavDFLBvSbWLOOCMhIg-d2JC3UukFUiDyaCJs5F2l2bC8j7kZKee9VMIlzVdq4OOdkku0vF_JYCWGKvmjBYvIJsudAiqpbs4byzGySDiWXYnFVZvEPoa4txCddmkqXDCCni9nEJ4bavyfC9b3E1KnA'}
    )
driver.add_cookie(
    {'domain': '.cnblogs.com', 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}
    )
driver.add_cookie({'domain': '.cnblogs.com', 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
                   'value': 'GA1.2.1690944654.1627368344'}
                  )

driver.refresh()


