# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 19:09:05 2021

@author: Henry Yang
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 
                   "M," "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", 
                   "Y", "Z"]
        index = []
        while n > 26:
            index.append(n//26-1)
            n = n%26
        index.append(n-1)
        ans = [letters[x] for x in index]
        ans = ''.join(ans)
        return ans
    