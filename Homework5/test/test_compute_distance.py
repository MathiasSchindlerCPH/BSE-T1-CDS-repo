#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 13:34:33 2021

@author: sandravicariaaguilar
"""

from geopy import distance

list_points = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]

def compute_distance(my_list):
    return list(map(lambda point: distance.distance(point[0], point[1]).km, my_list))


import pandas as pd
from pandas.testing import assert_series_equal
import unittest

class TestComputeDistance(unittest.TestCase): 
    
    def test_distance(self):
        list_points = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
        output = compute_distance(list_points)
        expected_output = [31.13186522205239, 157.005827868894]
        self.assertEqual(output, expected_output)
        
    def test_input_value(self): 
        self.assertRaises(TypeError, compute_distance, True)
        
        
if __name__ == '__main__':
    unittest.main()       
        
        
        
