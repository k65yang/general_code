# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 19:08:12 2021

@author: Henry Yang
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        currentIndex = 0
        numJumps = nums[currentIndex]
        lastIndex = len(nums)-1
        
        if (currentIndex == lastIndex):
            return True
        else:
            while (currentIndex != lastIndex and numJumps > 0):
                nextIndex = currentIndex + numJumps
                if (nextIndex > lastIndex):
                    return True
                elif (Solution().canJump(nums[nextIndex:])):
                    return True
                else:
                    numJumps -= 1
                
        return False