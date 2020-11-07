#!/bin/python3

import math
import os
import random
import re
import sys

def dec_to_bin(dec):
    return bin(dec).replace("0b","")

if __name__ == '__main__':
    n = int(input())
    binary = dec_to_bin(n)
    bits1_list = binary.split('0')
    
    ones = 0
    for bits1 in bits1_list:
        if len(bits1) > ones:
            ones = len(bits1)
            
    print(ones)
