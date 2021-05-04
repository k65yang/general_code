# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:50:34 2020

@author: Henry Yang
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def addTwoNumbersLocal(l1, l2, carry_digit):
            if l1.next is None and l2.next is None:
                single = (l1.val + l2.val + carry_digit)%10
                carry_digit = (l1.val + l2.val + carry_digit)//10
                
                if carry_digit == 1:
                    return ListNode(single, ListNode(1))
                else:
                    return ListNode(single)
                    
            elif l1.next is None:
                single = (l1.val + l2.val + carry_digit)%10
                carry_digit = (l1.val + l2.val + carry_digit)//10

                return ListNode(single, addTwoNumbersLocal(ListNode(0), l2.next, carry_digit))
            
            elif l2.next is None:
                single = (l1.val + l2.val + carry_digit)%10
                carry_digit = (l1.val + l2.val + carry_digit)//10

                return ListNode(single, addTwoNumbersLocal(l1.next, ListNode(0), carry_digit))
            
            else:
                single = (l1.val + l2.val + carry_digit)%10
                carry_digit = (l1.val + l2.val + carry_digit)//10

                return ListNode(single, addTwoNumbersLocal(l1.next, l2.next, carry_digit))
            
        addTwoNumbersLocal(l1, l2, 0)