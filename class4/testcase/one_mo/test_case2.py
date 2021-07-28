# -*- coding: utf-8 -*-
# @Time : 2021/7/28 11:51
# @Author : Limusen
# @File : test_case_2


# 　断言联系

import time
import unittest


class TestCase02(unittest.TestCase):

    def setUp(self) -> None:
        # print("执行前置")
        pass

    def tearDown(self) -> None:
        # print("执行后置信息")
        pass

    def test_case01(self):
        a = 1 == 1
        self.assertTrue(a, '断言失败,不是True')

    # def test_case02(self):
    #     a =1 ==3
    #     self.assertTrue(a,'断言失败,不是True')

    def test_case03(self):
        str = "星梦想"
        self.assertTrue(str.__contains__("梦想"))

    def test_case04(self):
        name = ['张三', '李四', '王五']
        self.assertIn('李四', name)
        print("范围测试")

    def test_case05(self):
        self.assertIsInstance('lishou', str)
        print("类型判定")


# if __name__ == "__main__":
#     unittest.main()
