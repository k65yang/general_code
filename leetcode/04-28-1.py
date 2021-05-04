# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 16:47:20 2021

@author: Henry Yang
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None:
            return 0
        else:
            curLength = 0
            curCharacters = []
            longestSub = 0
            for character in s:
                if not character in curCharacters:
                    curLength += 1
                    curCharacters.append(character)
                    if curLength > longestSub:
                        longestSub = curLength
                else:
                    indexRepeat = curCharacters.index(character)
                    curCharacters = curCharacters[indexRepeat + 1:]
                    curCharacters.append(character)
                    curLength -= indexRepeat
            return longestSub

                    