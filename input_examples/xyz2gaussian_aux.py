#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A collection of functions for xyz2gaussian

Created on Thu Sep  2 08:32:04 2021

@authors: A. Gomółka, T. Borowski
"""
import math, string

digits = string.digits

def count_lines(file):
    """
    Counts number of lines in a file

    Parameters
    ----------
    file : file object

    Returns
    -------
    i: int
        number of lines in a file
    """
    file.seek(0)
    i = -1
    for i, l in enumerate(file):
        pass
    file.seek(0)
    return i + 1


def int_digits(n):
    """
    For a positive integer n returns its number of digits 

    Parameters
    ----------
    n : INT

    Returns
    -------
    digits : INT

    """
    digits = int(math.log10(n))+1
    return digits


def read_head_tail(file):
    file.seek(0)
    str_file = file.read()
    file.seek(0)
    return str_file

    
def read_body(file):
    n_lines = count_lines(file)
    pass
        
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    