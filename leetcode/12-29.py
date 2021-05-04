# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 11:54:54 2020

@author: Henry Yang
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        if needle == "" or haystack == needle:
            return 0
        else:
            while i < len(haystack) - len(needle) + 1:
                if haystack[i] == needle[0]:
                    if haystack[i:i+len(needle)] == needle:
                        return i
                i += 1
            return -1