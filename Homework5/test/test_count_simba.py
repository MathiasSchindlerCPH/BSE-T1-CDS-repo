#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 14:02:51 2021

@author: sandravicariaaguilar
"""
# 6)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#

ex = ["Simba and Nala are lions.", "I laugh in the face of danger.",
 "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 

def count_simba(string):
    return sum(map(lambda i: i.count('Simba'), string))
    

list_2 = [2,4,5]

    
import pandas as pd
from pandas.testing import assert_series_equal
import unittest

class TestCountSimba(unittest.TestCase):
    def test_string(self):
        ex = ["Simba and Nala are lions.",
              "Hakuna matata", 
              "Timon, Pumba and Simba are friends, but Simba could eat the other two."]
        output = count_simba(ex)
        expected_output = 3
        self.assertEqual(output, expected_output)
    def test_input_value(self): 
        self.assertRaises(AttributeError , count_simba, True)
            
if __name__ == '__main__':
    unittest.main()  
 


