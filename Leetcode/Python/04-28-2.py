# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 17:14:49 2021

@author: Henry Yang
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = s[0]
        ansLength = len(ans)
        sLength = len(s)
        for i in range(sLength):
            for j in range(sLength-1, i, -1):
                if j-i+1 > ansLength and s[i] == s[j]:
                    isPalidrome = True
                    toCheck = s[i:j+1]
                    toCheckLength = len(toCheck)
                    for k in range(toCheckLength//2):
                        if toCheck[k] != toCheck[-1-k]:
                            isPalidrome = False
                            break
                    if isPalidrome:
                        ans = toCheck
                        ansLength = toCheckLength
        return ans