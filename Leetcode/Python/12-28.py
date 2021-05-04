# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 13:02:05 2020

@author: Henry Yang
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        correct = ""
        close = ""
        for brac in s:
            if brac == "(":
                correct += brac
                close = ")" + close
            elif brac == "[":
                correct += brac
                close = "]" + close
            elif brac == "{":
                correct += brac
                close = "}" + close
            else:
                if close == "" or brac != close[0]:
                    return False
                else:
                    correct += close[0]
                    close = close[1:]
                
        return correct + close == s