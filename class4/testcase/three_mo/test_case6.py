# -*- coding: utf-8 -*-
# @Time : 2021/7/28 16:44
# @Author : Limusen
# @File : test


import unittest


class TestCase06(unittest.TestCase):

    def test_case01(self):
        print("正在运算test_case01")
        self.assertEqual(3 + 4, 7, "求和失败")

    @unittest.skip("无条件跳过")
    def test_case02(self):
        '''无条件跳过'''
        print("正在运算test_case02")
        self.assertEqual(4 + 4, 8, "求和失败")

    @unittest.skipIf(True, '条件为真跳过')
    def test_case03(self):
        '''条件为真跳过'''
        print("正在运算test_case03")
        self.assertEqual(4 + 4, 8, "求和失败")

    # @unittest.skipIf(False, '条件为假不跳过')
    @unittest.skip("无条件跳过")
    def test_case04(self):
        '''无条件跳过'''
        print("正在运算test_case04")
        self.assertEqual(4 + 4, 9, "求和失败")

    @unittest.skipUnless(False, '条件为假跳过')
    def test_case05(self):
        '''条件为假跳过'''
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


if __name__ == "__main__":
    # # 方法一:加载测试类下面的所有用例
    # suite01 = unittest.TestLoader().loadTestsFromTestCase(TestCase06)
    # unittest.main(defaultTest='suite01')
    #
    # # 方法二：加载测试模块下面的所有用例
    # # 　先导入模块 自己
    # suite02 = unittest.TestLoader().loadTestsFromModule(test_case6)
    # unittest.main(defaultTest="suite02")
    #
    # # 方法三：使用字符串的方式加载用例
    # suite03 = unittest.TestLoader().loadTestsFromName('test_case6.TestCase06.test_case01')
    # # 整个模块
    # suite04 = unittest.TestLoader().loadTestsFromName('test_case6.TestCase06')
    # suite05 = unittest.TestLoader().loadTestsFromName('test_case6')
    #
    # # 单个加载全部测试用例
    # all_suite = unittest.TestSuite()
    # all_suite.addTests(suite01)
    # all_suite.addTests(suite02)
    # all_suite.addTests(suite03)
    # all_suite.addTests(suite04)
    # all_suite.addTests(suite05)
    pass
