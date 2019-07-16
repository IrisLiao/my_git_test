#!/usr/bin/python
# -*- coding:utf-8 -*-

'''



'''

import unittest
from utils.HTMLTestRunner import HTMLTestRunner
import time
import os
from utils.common import get_parent_path


if __name__ == '__main__':

    root_path = get_parent_path(os.getcwd())
    case_path = os.path.join(root_path, 'case')
    report_path = os.path.join(root_path,'report')
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    report_path = os.path.join(report_path,"auto_result_"+now+".html")
    report_file = open(report_path,'wb')

    runner = HTMLTestRunner(stream=report_file,title=u'自动化测试报告',description='执行测试结果')
    cases = unittest.defaultTestLoader.discover(case_path, pattern="testLogin.py", top_level_dir=None)
    runner.run(cases)
    report_file.close()
