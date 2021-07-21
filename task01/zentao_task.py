# -*- coding: utf-8 -*-
# @Time : 2021/7/19 15:22
# @Author : Limusen
# @File : zentao_task

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def zentao():
    driver = webdriver.Chrome()
    driver.get("http://47.107.178.45/zentao/www/index.php?m=user&f=login&referer=L3plbnRhby93d3cvaW5kZXgucGhwPw==")
    driver.implicitly_wait(15)

    driver.find_element(By.XPATH, '//input[@id="account"]').send_keys("test")
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("newdream123")
    driver.find_element(By.CSS_SELECTOR, 'button#submit.btn.btn-primary').click()
    time.sleep(2)

    # 点击测试(qa)tab
    driver.find_element(By.XPATH, '//ul[@class="nav nav-default"]/li[@data-id="qa"]').click()
    # 点击bug按钮
    driver.find_element(By.XPATH, '//li[@data-id="bug"]').click()
    time.sleep(1)
    # 点击提交bug按钮
    driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-primary').click()
    time.sleep(2)
    # 点击所属模块
    driver.find_element(By.XPATH,
                        '//*[@class="chosen-container chosen-container-single chosen-with-search" and @id="module_chosen"]').click()
    time.sleep(2)
    # 选择统计分析
    driver.find_element(By.XPATH, '//*[@id="module_chosen"]/div/ul/li[1]').click()
    time.sleep(1)
    # 点击所属项目
    driver.find_element(By.XPATH,
                        '//*[@class="chosen-container chosen-container-single chosen-with-search" and @id="project_chosen"]').click()
    # 点击db1
    driver.find_element(By.XPATH, '//*[@class="active-result" and @title="DBShopv1.0"]').click()
    time.sleep(1)

    # 点击影响版本
    time.sleep(2)
    driver.find_element(By.XPATH,'//div[@id="openedBuild_chosen"]/*[@class="chosen-choices"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="openedBuild_chosen"]/div/ul/li[1]').click()
    time.sleep(2)
    # 输入bug标题
    driver.find_element(By.XPATH,'//*[@class="input-control has-icon-right required"]/*[@name="title" and @id="title"]').send_keys("ui自动化测试提交bug!")


    # iframe框架切换
    iframe_path = '//*/iframe[@class="ke-edit-iframe"]'
    driver.switch_to.frame(driver.find_element(By.XPATH,iframe_path))
    driver.find_element(By.XPATH,'//*/body[@class="article-content"]').send_keys("[步骤] 打开 [结果] 坏的 [期望] 好的 ")
    driver.switch_to.default_content()

    driver.find_element(By.XPATH,'//*[@class="text-center form-actions"]/*[@id="submit" and @type="submit"]').click()

    time.sleep(2)


if __name__ == "__main__":
    zentao()
