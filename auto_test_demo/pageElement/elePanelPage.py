#!/usr/bin/python
# -*- coding:utf-8 -*-

"""

pannel page elements

"""

from selenium.webdriver.common.by import By


class ElePanelPage:

    write_article = (By.XPATH, '//*[@id="menu-posts"]/a/div[3]')
    # display_name
    display_name = (By.XPATH, '//*[@id="wp-admin-bar-my-account"]/a/span')
