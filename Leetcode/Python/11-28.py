# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:31:17 2020

@author: Henry Yang
"""

class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        begin = 0
        end = len(nums)-1
        moves = 0
        sums = []
        
        while begin < end:
            sums.append(nums[begin]+nums[end])
            begin += 1
            end -= 1
        
        print(sums)
        sums = [s - limit for s in sums]
        print(sums)
        sums_pos = [s>=0 for s in sums]
        print(sums_pos)
        sums_neg = [s<0 for s in sums]
        print(sums_neg)
        if sums_pos[0]>abs(sums_neg[0]):
            first = abs(sums_neg[0])
        else:
            first = sums_pos[0]
        print(sums)
        sums.remove(first)
        sums.insert(0, first)
        sums.sort()
        print(sums)
        most_frequent = max(set(sums), key = sums.count)
        print(most_frequent)
        
        for s in sums:
            if s != most_frequent:
                if abs(most_frequent - s) >= limit:
                    moves += 2
                else:
                    moves += 1
        
        return moves