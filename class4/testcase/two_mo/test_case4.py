# -*- coding: utf-8 -*-
# @Time : 2021/7/28 16:15
# @Author : Limusen
# @File : test_case4


import unittest


class TestCase04(unittest.TestCase):

    def test_case01(self):
        print("正在运算test_case01")
        self.assertEqual(3 + 4, 7, "求和失败")

    @unittest.skip("无条件跳过")
    def test_case02(self):
        print("正在运算test_case02")
        self.assertEqual(4 + 4, 8, "求和失败")

    @unittest.skipIf(True, '条件为真跳过')
    def test_case03(self):
        print("正在运算test_case03")
        self.assertEqual(4 + 4, 8, "求和失败")

    @unittest.skipIf(False, '条件为假不跳过')
    def test_case04(self):
        print("正在运算test_case04")
        self.assertEqual(4 + 4, 9, "求和失败")

    @unittest.skipUnless(False, '条件为假跳过')
    def test_case05(self):
        print("正在运算test_case05")
        self.assertEqual(4 + 4, 9, "求和失败")

    @unittest.expectedFailure  # 失败不记录失败数量
    def test_case06(self):
        print("正在运算test_case06")
        self.assertEqual(4 + 4, 9, "求和失败")

    @unittest.expectedFailure
    def test_case07(self):
        print("正在运算test_case07")
        self.assertEqual(4 + 4, 9, "求和失败")

#
# if __name__ == "__main__":
#     unittest.main()
