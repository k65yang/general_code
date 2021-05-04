# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 11:43:31 2020

@author: Henry Yang
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        digits.reverse()
        carry = 0
        for i in range(len(digits)):
            digits[i] = digits[i] + carry
            carry = 0
            if digits[i] > 9:
                carry = digits[i]//10
                digits[i] = digits[i]%10
        if carry != 0:
            digits.append(carry)
        digits.reverse()
        return digits