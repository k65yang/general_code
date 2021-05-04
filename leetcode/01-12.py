# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:53:44 2021

@author: Henry Yang
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = 0
        while index1 < len(numbers)-1:
            valIndex2 = target-numbers[index1]
            if valIndex2 in numbers[index1:]:
                return [index1+1, numbers[index1+1:].index(valIndex2)+index1+2]
            discard_value = numbers[index1]
            index1 += 1
            while numbers[index1] == discard_value:
                index1 += 1
        return False