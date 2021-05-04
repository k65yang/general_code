# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 15:49:30 2020

@author: Henry Yang
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        while m < m + n:
            print(m)
            print(i)
            nums1[m] = nums2[i]
            i += 1
            m += 1
        