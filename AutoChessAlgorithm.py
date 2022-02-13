#!/usr/bin/python3  
# -*- coding: utf-8 -*-
"""
author: tuzichun

"""
import numpy as np
import pandas as pd
from itertools import combinations
 
 
class Chess(object):
    # 初始化中给对象属性赋值
    def __init__(self, trammels_x, trammels_y, name):
        self.X = trammels_x
        self.Y = trammels_y
        self.NAME = name
 
    def __str__(self):
        return self.NAME
 
 
class Possibility(object):
    def __init__(self, chess_list):
        self.object_list = chess_list
        x_set = set()
        y_set = set()
        value_set = set()
        for wtf in self.object_list:
            x_set.add(wtf.X)
            y_set.add(wtf.Y)
            value_set.add(wtf.NAME)
        self.value = len(x_set) + len(y_set)
        self.count = len(value_set)
 
    def __str__(self):
        result = ""
        for wtf in self.object_list:
            result = result.join(wtf.NAME) + ","
        return result
 
 
def generate_chess():
    # 读取数据
    result = []
    csv_result = pd.read_csv("2321.csv", index_col=0)
    index_count = csv_result.shape[0]
    column_count = csv_result.shape[1]
    for wtf_x in range(0, index_count):
        for wtf_y in range(0, column_count):
            value = csv_result.iloc[wtf_x, wtf_y]
            if value != np.NAN:
                result.append(Chess(wtf_x, wtf_y, value))
    return result
 
 
if __name__ == '__main__':
 
    Chess_list = generate_chess()
 
    dataframe_result = pd.DataFrame(columns=['combination', 'value', 'count'])
 
    for x in range(3, 11):
        dataframe_result_part = pd.DataFrame(columns=['combination', 'value', 'count'])
        a = []
        res = list(combinations(Chess_list, x))
        if len(res) != 0:
            for y in res:
                y = list(y)
                deal = Possibility(y)
                if deal.value != 2 * x:
                    dataframe_result_part['combination'].append(str(deal))
                    dataframe_result_part['value'].append(deal.value)
                    dataframe_result_part['count'].append(deal.count)
        else:
            continue
        dataframe_result.append(dataframe_result_part)
    dataframe_result = dataframe_result.sort_values(by=["value", "count"], ascending=(True, False))
    dataframe_result.to_csv("1.csv")
