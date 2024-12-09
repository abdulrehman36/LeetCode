#You are given an array prices where prices[i] is the price of a given stock on the ith day.

#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        min_price = prices[0]  # Minimum price so far
        max_profit = 0  # Maximum profit we can achieve

        for price in prices[1:]:
            # Update max profit if we sell at the current price
            max_profit = max(max_profit, price - min_price)

            # Update min price to ensure we're buying at the lowest possible price
            min_price = min(min_price, price)

        return max_profit

solution_instance = Solution()
result = solution_instance.maxProfit([1,2,3,4,5,1])

print(result)