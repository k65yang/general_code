# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:34:42 2021

@author: Henry Yang
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        priceLength = len(prices)
        ans = 0
        if prices is None or priceLength == 0:
            return ans
        
        searchedPrice = []
        i = 0
        
        while i < priceLength-1:
            currentPrice = prices[i]
            if all(currentPrice < i for i in searchedPrice):
                maxSellPrice = max(prices[i+1:])
                diff = maxSellPrice - prices[i]
                if diff > ans:
                    ans = diff
                searchedPrice.append(prices[i])
            i += 1
        return ans
        
        # ans = 0
        # pricesLength = len(prices)
        # if prices is None or pricesLength == 0:
        #     return ans
        # elif pricesLength == 1:
        #     return prices[0]
            
        # lowestPrice = min(prices)
        # lowestPriceIndex = prices.index(lowestPrice)
        
        # highestPrice = max(prices)
        # highestPriceIndex = prices.index(highestPrice)
        
        # if highestPriceIndex > lowestPriceIndex:
        #     return highestPrice - lowestPrice
        # else:
        #     pseudoMax = max(prices[:lowestPriceIndex
        
        # if lowestPriceIndex == len(prices)-1:
        #     return ans
        # else:
        #     highestPrice = max(prices[lowestPriceIndex+1:])
        #     return highestPrice - lowestPrice
        