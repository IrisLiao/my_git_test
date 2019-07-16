#!/usr/bin/python
# -*- coding:utf-8 -*-

'''

base functions

'''

import os
import time
from selenium import webdriver
from utils.logger import logger

logger = logger(logger = 'basePage').getlog()


class BasePage(object):

    def __init__(self, driver=None):
        if driver is None:
            os.system("taskkill /im chromedriver.exe /f")
            self.driver = webdriver.Chrome()
            # self.driver.get("http://autotest/wordpress/wp-login.php")
        else:
            self.driver = driver

    def get_element(self,*locator):
        logger.info('查找元素 %s' % str(locator))
        return self.driver.find_element(*locator)

    # 获取元素，智能等待
    def wait_element(self,*locator):
        ele = None
        count = 0
        while ele is None:
            count += 1
            try:
                ele = self.driver.find_element(*locator)
            except():
                pass
            flag = ele is not None  # ??
            logger.info('查找元素第%d次 %s %s ' %(count,flag,str(locator)))
            time.sleep(0.1)
            if count > 99:
                logger.info('没有找到元素 %s' % str(locator))
                break
        return ele

    # close driver and window
    def close_window(self):
        self.driver.close()
        self.driver.quit()
