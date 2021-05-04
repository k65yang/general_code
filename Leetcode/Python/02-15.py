# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:07:49 2021

@author: Henry Yang
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        velocity = [[0,1], [1,0], [0,-1], [-1,0]]
        currentVelocityIndex = 0
        visited = []
        currentCoor = [0,0]
        result = []
        
        while (not currentCoor in visited):
            result.append(matrix[currentCoor[0]][currentCoor[1]])
            visited.append(currentCoor)
            nextCoor = [sum(coor) for coor in zip(currentCoor,velocity[currentVelocityIndex])]
            if (nextCoor[0] > len(matrix)-1 or nextCoor[1] > len(matrix[0])-1 or 
                nextCoor[0] < 0 or nextCoor [1] < 0 or nextCoor in visited):
                if currentVelocityIndex == 3:
                    currentVelocityIndex = 0
                else:
                    currentVelocityIndex += 1
                currentCoor = [sum(coor) for coor in zip(currentCoor,velocity[currentVelocityIndex])]
            else:
                currentCoor = nextCoor
        
        return result