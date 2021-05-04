# -*- coding: utf-8 -*-
"""
Created on Sat May  1 17:55:32 2021

@author: Henry Yang
"""

class Solution:
    def generateParenthesis(self, n:"int") -> list:
        left = "("
        right = ")"
        ans = []
        counter = 1
        while counter <= n:
            if counter == 1:
                ans.append(left + right)
            else:
                toIterate = ans[:]
                ans = []
                for combination in toIterate:
                    ans.append(left + combination + right)
                    ans.append(left + right + combination)
                    ans.append(combination + left + right)
                    if counter%2 == 0 and counter != 2:
                        halfAsList = [left for _ in range(int(counter/2))] + [right for _ in range(int(counter/2))]
                        half = "".join(halfAsList)
                        ans.append(half + half)
                    ans = list(dict.fromkeys(ans))
            counter += 1
        return ans