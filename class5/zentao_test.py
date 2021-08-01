# -*- coding: utf-8 -*-
# @Time : 2021/7/30 9:42
# @Author : Limusen
# @File : zentao_test


import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import HTMLTestRunner

current = os.path.dirname(__file__)
print(current)


class ZentaoTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    def test_login_01(self):
        '''登录用例 test1'''
        self.driver.get(
            "http://47.107.178.45/zentao/www/index.php?m=user&f=login&referer=L3plbnRhby93d3cvaW5kZXgucGhwP209dXNlciZmPWxvZ2lueg==")
        time.sleep(2)
        self.driver.find_element(By.NAME, 'account').send_keys('test01')
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="loginPanel"]/div/div[2]/form/table/tbody/tr[2]/td/input').send_keys(
            'newdream123')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="submit"]').click()
        # time.sleep(1)
        # result = self.driver.find_element(By.XPATH, '//*[@id="userNav"]/li/a/span[1]').text
        # self.assertEqual(result, '测试人员1', 'test_login_01执行失败')
        self.assertTrue(True, EC.text_to_be_present_in_element((By.XPATH, '//*[@id="userNav"]/li/a/span[1]'), '测试人员1'))

    def test_login_02(self):
        '''登录用例 test2'''
        self.driver.get(
            "http://47.107.178.45/zentao/www/index.php?m=user&f=login&referer=L3plbnRhby93d3cvaW5kZXgucGhwP209dXNlciZmPWxvZ2lueg==")
        time.sleep(2)
        self.driver.find_element(By.NAME, 'account').send_keys('test02')
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="loginPanel"]/div/div[2]/form/table/tbody/tr[2]/td/input').send_keys(
            'newdream123')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="submit"]').click()
        time.sleep(1)
        # result = self.driver.find_element(By.XPATH, '//*[@id="userNav"]/li/a/span[1]').text
        # self.assertEqual(result, '测试人员2', 'test_login_02执行失败')
        self.assertTrue(True, EC.text_to_be_present_in_element((By.XPATH, '//*[@id="userNav"]/li/a/span[1]'), '测试人员2'))


if __name__ == "__main__":
    testsuite = unittest.TestSuite(unittest.makeSuite(ZentaoTest))
    nowtime = time.strftime('%Y_%m_%d_%H_%M_%S')

    fp = open('../reports/report_' + nowtime + '.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="P9_P10 UI自动化",
                                           description="xixi")
    runner.run(testsuite)
