# -*- coding: utf-8 -*-
# @Time : 2021/7/19 14:49
# @Author : Limusen
# @File : qzeon_tash

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def Qzen():

    drvier = webdriver.Chrome()
    drvier.get("https://qzone.qq.com/")
    drvier.implicitly_wait(10)

    drvier.switch_to.frame(drvier.find_element(By.ID,'login_frame'))
    drvier.find_element(By.XPATH,'//span[@id="img_out_1695403591"]').click()
    time.sleep(2)
    drvier.find_element(By.XPATH,'//*[@id="$1_substitutor_content"]').click()
    time.sleep(2)
    drvier.find_element(By.XPATH,'//*[@id="$1_content_content"]').send_keys("ui自动化测试")
    time.sleep(2)
    drvier.find_element(By.XPATH,'//div[@class="op"]').click()
    time.sleep(2)
    drvier.quit()

if __name__ == "__main__":
    Qzen()