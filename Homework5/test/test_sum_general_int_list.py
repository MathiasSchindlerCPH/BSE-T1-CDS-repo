#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 13:34:33 2021

@author: sandravicariaaguilar
"""

# 9)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13 
#

list_numbers = [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]

def sum_general_int_list(list_n):
    if type(list_n) != list:
        return list_n
    if list_n == []:
        return 0
    return sum_general_int_list(list_n[0]) + sum_general_int_list(list_n[1:])

print(sum_general_int_list(list_numbers))

import pandas as pd
from pandas.testing import assert_series_equal
import unittest

class TestSumGeneralIntList(unittest.TestCase): 
    
    def test_sum_general_int_list(self):
        list_numbers = [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]
        list_a = []
        output = sum_general_int_list(list_numbers)
        expected_output = 48
        self.assertEqual(output, expected_output)
        output_0 = sum_general_int_list(list_a)
        expected_output_0 = 0 
        self.assertEqual(output_0, expected_output_0)
        
        
    def test_input_value(self): 
        self.assertRaises(TypeError, sum_general_int_list, True)
  
if __name__ == '__main__':
    unittest.main()
        
       
        
        
        
