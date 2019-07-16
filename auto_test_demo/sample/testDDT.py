#!/usr/bin/python
# -*- coding:utf-8 -*-

'''



'''

import unittest
from ddt import ddt,data,unpack
import time


@ddt
class TestDDTAndReport(unittest.TestCase):

    @data(1,2,3)
    def test_one_param(self,num):
        print('test one param:')
        print(self.my_add(num,1))
        result = self.my_add(num,1)
        self.assertEqual(result,num+1,'calculation error!')
        time.sleep(0.1)

    @data((10,1),(20,1),(30,1))
    @unpack
    def test_two_param(self,num1,num2):
        print('test two param:')
        print(self.my_add(num1,num2))
        result = self.my_add(num1, num2)
        self.assertEqual(result, num1 + num2, 'calculation error!')
        time.sleep(0.1)

    def my_add(self,a,b):
        return a + b

if __name__ == '__main__':
    unittest.main()
