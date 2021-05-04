# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 19:09:52 2021

@author: Henry Yang
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        zigzagMatrix = [[] for _ in range(numRows)]
        currentRow = 0
        isIncrementRow = True
        for character in s:
            zigzagMatrix[currentRow].append(character)
            if isIncrementRow:
                currentRow += 1
                if currentRow == numRows-1:
                    isIncrementRow = False
            else:
                currentRow -= 1
                if currentRow == 0:
                    isIncrementRow = True
        ans = []
        for row in zigzagMatrix:
            ans += row
        return "".join(ans)