# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 12:40:08 2020

@author: Henry Yang
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def climbStairs(n):
            if n == 0:
                return 1
            elif n == 1:
                return climbStairs(n - 1)
            else:
                return climbStairs(n - 1) + climbStairs(n - 2)
        return climbStairs(n)