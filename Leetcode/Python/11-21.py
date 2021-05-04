# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 18:31:49 2020

@author: Henry Yang
"""

class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def isFair(loi):
            sum_even = 0
            sum_odd = 0
            for n in range(len(loi)):
                if n%2 == 0:
                    sum_even += loi[n]
                else:
                    sum_odd += loi[n]
            return sum_even == sum_odd
        
        fair_indices = 0

        for i in range(len(nums)):
            test_nums = nums[:]
            test_nums.pop(i)
            if isFair(test_nums):
                fair_indices += 1
        
        return fair_indices