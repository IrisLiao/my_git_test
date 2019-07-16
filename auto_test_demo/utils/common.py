#!/usr/bin/python
# -*- coding:utf-8 -*-

'''



'''

import os
import csv


# get parent path
def get_parent_path(current_path):

    return os.path.abspath(os.path.dirname(current_path) + os.path.sep + '.')


# get data from csv
def get_csv_data(filename):

    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            data.append(row)
    return data


