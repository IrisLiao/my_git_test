#!/usr/bin/python
# -*- coding:utf-8 -*-

'''

login page elements

'''

from selenium.webdriver.common.by import By


class EleLoginPage:

    user_name = (By.ID, 'user_login')
    password = (By.ID, 'user_pass')
    login_btn = (By.ID, 'wp-submit')
    error_msg = (By.ID, 'login_error')

