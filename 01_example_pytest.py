#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 09:38:59 2019

@author: pughd
"""


# Create a class to hold our tests
class TestClass:

    def test_one(self):
        assert small_function(2,5) == 7
    
    def test_two(self):
        assert small_function(2,6) == 85
        
    def test_three(self):
        assert small_function(2,89) == 85
        
    def test_four(self):
        assert small_function(235,89) == 100
        
        
# Define our function
def small_function(x,y):
    if x< 100:
        return x + y
    else:
        return 100
