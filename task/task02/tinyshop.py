# -*- coding: utf-8 -*-
# @Time : 2021/7/23 9:53
# @Author : Limusen
# @File : tinyshop


import time
import random
from icecream import ic
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def scrollby(driver, coordinate):
    time.sleep(2)
    js = "window.scrollBy(0," + str(coordinate) + ")"
    driver.execute_script(js)


def tinyshop(coordinate):
    driver = webdriver.Chrome()
    driver.get("http://47.107.178.45/tinyshop/")
    driver.maximize_window()
    driver.implicitly_wait(15)

    driver.find_element(By.XPATH, '//*[@class="item"]//*[@href="/tinyshop/index.php?con=simple&act=login"]').click()
    driver.find_element(By.XPATH, '//*[@class="input" and @id="account"]').send_keys("lishouwu@qq.com")
    driver.find_element(By.XPATH, '//*[@class="input" and @name="password"]').send_keys("123456")
    driver.find_element(By.XPATH, '//*[@class="btn btn-main "]').click()
    time.sleep(2)

    scrollby(driver, coordinate)

    driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[2]/div[2]/div[2]/ul/li[1]/dl/dt/a/img').click()
    time.sleep(2)
    color_list = driver.find_elements(By.XPATH, '//*[@class="spec-values clearfix" and @spec_id="2"]/*')
    random.choice(color_list).click()
    time.sleep(2)
    size_list = driver.find_elements(By.XPATH, '//*[@class="spec-values clearfix" and @spec_id="6"]/*')
    random.choice(size_list).click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="add-cart" and @class="btn btn-main"]').click()

    action_move = driver.find_element(By.XPATH, '//*[@id="shopping-cart" and @class="shopping"]')
    ActionChains(driver).move_to_element(action_move).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,
                        '//*[@href="/tinyshop/index.php?con=simple&act=cart" and @class="btn btn-main"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH,
                        '//*[@href="/tinyshop/index.php?con=simple&act=order&cart_type=cart" and @class="btn btn-main"]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="address_other"]').click()
    time.sleep(1)
    print("---------------------------------------------------------------------")

    # 　切换表单
    iframe_path = driver.find_element(By.XPATH,
                                      "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe")
    driver.switch_to.frame(iframe_path)

    driver.find_element(By.XPATH, '//*[@id="province"]').click()

    address_list = driver.find_elements(By.XPATH, '//*[@id="province" and @name="province"]/*')
    random.choice(address_list).click()
    time.sleep(3)

    shi_list = driver.find_elements(By.XPATH, '//*[@id="city" and @name="city"]/*')
    random.choice(shi_list).click()
    time.sleep(3)

    qu_list = driver.find_elements(By.XPATH, '//*[@id="county" and @name="county"]/*')
    random.choice(qu_list).click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@type="text" and @name="zip"]').send_keys(430181)

    driver.find_element(By.XPATH, '//*[@name="addr"]').send_keys("xixixixixixi")
    driver.find_element(By.XPATH, '//*[@name="accept_name"]').send_keys("你说呢")
    driver.find_element(By.XPATH, '//*[@name="mobile"]').send_keys(15574987866)
    driver.find_element(By.XPATH, '//*[@name="phone"]').send_keys(15578219231)
    driver.find_element(By.XPATH, '//*[@type="submit" and @class="btn"]').click()

    dress_list = driver.find_elements(By.XPATH, '//*[@class="address-list clearfix"]/*')
    dress_list[-1].click()
    driver.switch_to.default_content()

    scrollby(driver, 1000)

    driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/form/div[6]/p/input').click()

    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/form/div[3]/p/input').click()

    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    tinyshop(1000)
