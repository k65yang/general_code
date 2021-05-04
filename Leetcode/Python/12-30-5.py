# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 13:10:33 2020

@author: Henry Yang
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        i = 0
        while i < len(nums):
            print("i")
            print([nums[i]])
            ans.append([nums[i]])
            j = 0
            stop = len(ans)-1
            lastIndex = len(ans)-1
            while j < stop:
                print("j")
                print(j)
                print(ans[j])
                sub = [s for s in ans[j]]
                end = [e for e in ans[lastIndex]]
                sub.extend(end)
                print(sub)
                ans.append(sub)
                j += 1
            i += 1
            print('ans')
            print(ans)
        ans.insert(0, [])
        return ans