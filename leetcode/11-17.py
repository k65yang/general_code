# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:17:38 2020

@author: Henry Yang
"""

class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        
        prev_ray = p
        ray = q
        wall = 1
        i = 0
        max_iter = 2000
        th = 0.05 * p
        while i < max_iter:
            if ray == 0 and wall != 0:
                return wall%4 - 1
            elif ray == p and wall != 3:
                return wall%4
            else:
                next_ray = (prev_ray * (p -ray))/ray
                prev_ray = round(p - ray, 2)
                if abs(next_ray - p) <= th:
                    ray = p
                elif next_ray <= th:
                    ray = 0
                else:
                    ray  = next_ray
                print(ray)
                i += 1
                wall += 1
