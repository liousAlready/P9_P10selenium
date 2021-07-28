# -*- coding: utf-8 -*-
# @Time : 2021/7/27 15:55
# @Author : Limusen
# @File : test_case1

import unittest


class TestCase01(unittest.TestCase):

    def setUp(self) -> None:
        print("执行前置")

    def tearDown(self) -> None:
        print("执行后置信息")

    def test_case01(self):
        self.assertEqual(1 + 2, 3)

    def test_case02(self):
        self.assertEqual(1 + 2, 2)


if __name__ == "__main__":
    TestCase01().test_case01()
    TestCase01().test_case02()
