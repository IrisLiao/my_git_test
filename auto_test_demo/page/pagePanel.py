#!/usr/bin/python
# -*- coding:utf-8 -*-

'''

pannel page functions

'''

from base.basePage import BasePage
from pageElement.elePanelPage import *


class PagePanel(BasePage):

    def __init__(self, driver=None):
        BasePage.__init__(self, driver)

    def click_write_article(self):
        self.wait_element(*ElePanelPage.write_article).click()

    # get login name
    def get_login_name(self):
        return self.wait_element(*ElePanelPage.display_name).text
