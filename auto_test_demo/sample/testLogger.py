#!/usr/bin/python
# -*- coding:utf-8 -*-

'''



'''

from utils.logger import logger

if __name__ == '__main__':
    logger = logger(logger='TestLog').getlog()
    logger.info('===test log===')