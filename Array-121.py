#You are given an array prices where prices[i] is the price of a given stock on the ith day.

#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                return prices[i]
        return 0

solution_instance = Solution()
result = solution_instance.containsDuplicate([1,2,3,4,5,1])

print(result)