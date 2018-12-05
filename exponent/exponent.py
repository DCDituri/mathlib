# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 15:53:41 2018

@author: dcdit
"""
def exp(a, b = 0):
    if (b == 0):
        if(a == 0):
            return "(undefined)"
        return 1
    elif (b > 0):
        ret = a
        for i in range(b-1):
            ret = ret * a
        return ret
    elif (b < 0):
        ret = 1/a
        for i in range(abs(b)-1):
            ret = ret / a
        return ret
