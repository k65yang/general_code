# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 21:50:45 2020

@author: Henry Yang
"""

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

TREE1 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))
TREE2 = TreeNode(5)
TREE3 = TreeNode(4, TreeNode(1, TreeNode(2, TreeNode(3))))

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def rob(t, canRob):
            if t is None:
                return 0
            else:
                if canRob:
                    skipHouse = rob(t.left, True) + rob(t.right, True)
                    robHouse =  t.val + rob(t.left, False) + rob(t.right, False)
                    if skipHouse > robHouse:
                        return skipHouse
                    else:
                        return robHouse
                else:
                    return rob(t.left, True) + rob(t.right, True)
        
        ans = rob(root, True)
        
        return ans