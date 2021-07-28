# -*- coding: utf-8 -*-
# @Time : 2021/7/28 17:02
# @Author : Limusen
# @File : run_all_testcase

import time
import os
import unittest
import HTMLTestRunner

#  执行层脚本，一次执行所有需要运行的测试脚本


curren_path = os.path.dirname(__file__)
start_path = os.path.join(curren_path + '' + '/class4')

discover = unittest.defaultTestLoader.discover(start_dir=start_path,
                                               pattern='test*.py',
                                               top_level_dir=start_path)

main_suite = unittest.TestSuite()
main_suite.addTest(discover)
# unittest.main(defaultTest='main_suite', verbosity=2)

# 报告文件名覆盖问题
# 生成时间戳来使用
nowtime = time.strftime('%Y_%m_%d_%H_%M_%S')

fp = open('report_'+nowtime+'.html', 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                       title="测试报告",
                                       description="xixi")
runner.run(main_suite)
