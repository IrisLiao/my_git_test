#!/usr/bin/python
# -*- coding:utf-8 -*-

"""

login page test cases

"""

import unittest
from time import sleep
from ddt import ddt, data, unpack
from utils.common import *
from utils.logger import logger
from page.pageLogin import PageLogin


logger = logger(logger='test_login').getlog()


@ddt
class TestLogin(unittest.TestCase):

    # get login info
    current_path = os.path.dirname(os.path.abspath(__file__))
    root_path = get_parent_path(current_path)
    account_info = get_csv_data(os.path.join(root_path, 'data', 'login_info.csv'))
    test_account_all = get_csv_data(os.path.join(root_path, 'data', 'user_all.csv'))
    test_account_failed = (("admin", "1234567", "The password you entered for the username admin is incorrect"), ("", "1234516", "The username field is empty"), ("admin2", "", "The password field is empty"))

    @classmethod
    def setUpClass(cls):
        logger.info('===Start Testing:===')
        cls.p_login = PageLogin()

    @classmethod
    def tearDownClass(cls):
        cls.p_login.close_window()
        logger.info('===End Testing!===')

    @data(*account_info)
    @unpack
    def test_login_pass(self, user, password, expected_result):

        self.p_login.driver.get('http://autotest/wordpress/wp-login.php')
        logger.info('===Login start:===')
        p_panel = self.p_login.login(user, password)
        actual_result = p_panel.get_login_name()
        logger.info('Expected login name: %s ' % expected_result)
        logger.info('Got actual login name: %s ' % actual_result)
        logger.info('===Start checking: ===')
        self.assertEqual(expected_result,actual_result, '=== Checked login name failed! ===')

        sleep(5)

    @data(*test_account_failed)
    @unpack
    def test_login_fail(self, user, password, expected_result):
        self.p_login.driver.get('http://autotest/wordpress/wp-login.php')
        p_panel = self.p_login.login(user, password)
        login_return_error_msg = self.p_login.get_error_msg()
        # logger.info('p_panel is : %s' % p_panel)
        logger.info('Expected error msg: %s' % expected_result)
        logger.info('Got actual error msg: %s' % login_return_error_msg)
        self.assertIn(expected_result,login_return_error_msg)

        sleep(5)

    @data(*test_account_all)
    @unpack
    def test_login_all(self, user, password, flag, expected_result):
        self.p_login.driver.get('http://autotest/wordpress/wp-login.php')
        p_panel = self.p_login.login(user, password)
        if flag == '1':
            actual_result = p_panel.get_login_name()
        else:
            actual_result = self.p_login.get_error_msg()
        logger.info('Expected result is %s' % expected_result)
        logger.info('Got actual result is %s' % actual_result)
        self.assertIn(expected_result, actual_result)

        sleep(5)


if __name__ == '__main__':

    unittest.main()
