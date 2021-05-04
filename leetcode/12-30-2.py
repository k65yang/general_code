# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 12:10:42 2020

@author: Henry Yang
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = list(reversed(a))
        b = list(reversed(b))
        print(a)
        print(b)
        ans = ""
        carry = 0
        i = 0
        while i < len(a) or i < len(b):
            if i >= len(a):
                binsum = int(b[i]) + carry
                if binsum == 0 or binsum == 1:
                    ans = str(binsum) + ans
                    carry = 0
                else:
                    ans = str(0) + ans
                    carry = 1
            elif i >= len(b):
                binsum = int(a[i]) + carry
                if binsum == 0 or binsum == 1:
                    ans = str(binsum) + ans
                    carry = 0
                else:
                    ans = str(0) + ans
                    carry = 1
            else:
                print("third")
                binsum = int(a[i]) + int(b[i]) + carry
                if binsum == 0 or binsum == 1:
                    ans = str(binsum) + ans
                    carry = 0
                elif binsum == 2:
                    ans = str(0) + ans
                    carry = 1
                else:
                    ans = str(1) + ans
                    carry = 1
            print(carry)
            i += 1
        if carry == 1:
            ans = str(carry) + ans
        return ans