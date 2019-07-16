#!/usr/bin/python
# -*- coding:utf-8 -*-

'''

login page functions

'''


from base.basePage import BasePage
from pageElement.eleLoginPage import *
from page.pagePanel import PagePanel


class PageLogin(BasePage):

    def __init__(self, driver=None):
        BasePage.__init__(self, driver)
        # driver.get('http://autotest/wordpress/wp-login.php')

    def login(self, name, password):

        self.wait_element(*EleLoginPage.user_name).clear()
        self.wait_element(*EleLoginPage.user_name).send_keys(name)
        self.wait_element(*EleLoginPage.password).clear()
        self.wait_element(*EleLoginPage.password).send_keys(password)
        self.wait_element(*EleLoginPage.login_btn).click()
        return PagePanel(self.driver)  # ??

    def get_error_msg(self):
        return self.wait_element(*EleLoginPage.error_msg).text


if __name__ == '__main__':
    pl = PageLogin()
    pl.login('admin','123456')
    print('')
    print('')
    print('')
    pl.close_window()
