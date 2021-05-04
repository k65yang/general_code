# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 11:35:28 2021

@author: Henry Yang
"""

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        parsedResult = []
        isPositive = True
        isFirst = True
        s = s.lstrip()
        for character in s:
            try:
                int(character)
                parsedResult.append(character)
            except ValueError:
                if isFirst and character == "-":
                    isPositive = False
                elif isFirst and character == "+":
                    pass
                else:
                    break
            isFirst = False

        if len(parsedResult) == 0:
            return result
        
        result = "".join(parsedResult)
        result = int(result)
        
        if not isPositive:
            result *= -1
            
        if result > (2**31)-1:
            result = (2**31)-1
        elif result < (-2)**31:
            result = (-2)**31
            
        return result