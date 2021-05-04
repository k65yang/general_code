# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 18:39:26 2021

@author: Henry Yang
"""

class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        #base = [2 for x in range(1,22)]
        #exp = [x for x in range(1,22)]
        good = [2**x for x in range(22)]
        ans = 0
        while len(deliciousness)> 0:
            end = deliciousness.pop()
            i = 0
            while i < len(deliciousness):
                if deliciousness[i] + end in good:
                    ans += 1
                i += 1
        return ans