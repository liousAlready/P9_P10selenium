# -*- coding: utf-8 -*-
# @Time : 2021/7/19 9:53
# @Author : Limusen
# @File : php_wind_task


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def output_wind():
    driver = webdriver.Chrome()
    driver.get("http://47.107.178.45/phpwind/")
    driver.maximize_window()
    driver.implicitly_wait(15)

    driver.find_element(By.ID, 'J_username').send_keys("limusen1")
    driver.find_element(By.ID, 'J_password').send_keys(123456)
    driver.find_element(By.CLASS_NAME, "btn.btn_big.btn_submit").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "header_post").click()

    # 　点击发帖模块
    # driver.find_element(By.CSS_SELECTOR,'#J_forum_list li+li+li.J_cate_item').click()
    # 优化取值的方法,采用 查找第n个元素方法 nth-child(n)
    driver.find_element(By.CSS_SELECTOR, '#J_forum_list li:nth-child(3)').click()
    time.sleep(1)
    # 选择版块
    # driver.find_element_by_css_selector('div#s-top-left a:nth-child(3)').click()
    # 优化取值的方法,采用 查找第n个元素方法 nth-child(n)
    driver.find_element(By.CSS_SELECTOR, '#J_forum_ul li:nth-child(3)').click()
    driver.find_element(By.ID, 'J_head_forum_sub').click()

    # 　输入帖子标题
    driver.find_element(By.ID, 'mainForm').find_element(By.CSS_SELECTOR,
                                                        'input#J_atc_title.length_6').send_keys(
        "测试发帖")
    # 获取iframe元素 两种方法都可以
    iframe_xpath = '//div[2]/iframe[@class="wind_editor_iframe"]'
    # iframe_xpath = '//*[@id="mainForm"]/div/nav/nav/div/div[3]/div[1]/div/div/div[2]/iframe'

    # 跳转进入iframe框架
    driver.switch_to.frame(driver.find_element(By.XPATH, iframe_xpath))
    driver.find_element(By.XPATH, "/html/body").send_keys("测试输入内容成功")
    # 跳出框架
    driver.switch_to.default_content()
    # 点击提交
    driver.find_element(By.XPATH, '//div/button[@id="J_post_sub"]').click()
    time.sleep(2)

    driver.quit()


if __name__ == "__main__":
    output_wind()
