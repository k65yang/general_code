# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 15:25:54 2021

@author: Henry Yang
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        inputLength = len(height)
        for i in range(inputLength):
            for j in range(inputLength-1,i,-1):
                area = min([height[i],height[j]]) * (j-i)
                if area > result:
                    result = area
        return result