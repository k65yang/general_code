# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 13:23:42 2020

@author: Henry Yang
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def mergeTwoListsLocal(l1, l2):
            if l1 is None and l2 is None:
                return None
            elif l1 is None:
                return ListNode(l2.val, mergeTwoListsLocal(None, l2.next))
            elif l2 is None:
                return ListNode(l1.val, mergeTwoListsLocal(l1.next, None))
            else:
                val1 = l1.val
                val2 = l2.val
                if val1 < val2:
                    return ListNode(l1.val, mergeTwoListsLocal(l1.next, l2))
                else:
                    return listNode(l2.val, mergeTwoListsLocal(l1, l2.next))
        return mergeTwoListsLocal(l1,l2)