# -*- coding: utf-8 -*-
# @Time : 2021/7/28 16:01
# @Author : Limusen
# @File : test_case3

import time
import unittest


class TestCase03(unittest.TestCase):

    def test_case01_aaa(self):
        print("执行用例:test_aaa")

    def test_case02_ddd(self):
        print("执行用例:test_ddd")

    def test_case03_ccc(self):
        print("执行用例:test_ccc")

    def test_case04_bbb(self):
        print("执行用例:test_bbb")

#
# if __name__ == "__main__":
#     # unittest.main()
#
#     # # 改变执行顺序方法
#     # suite = unittest.TestSuite()
#     # suite.addTest(TestCase03('test_bbb'))
#     # suite.addTest(TestCase03('test_ccc'))
#     # unittest.main(defaultTest='suite')
#     pass
#
#     # 改名字 test_case04_bbb
#     unittest.main()
