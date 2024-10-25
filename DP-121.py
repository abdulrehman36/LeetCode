class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # base case
        if not prices or len(prices) == 1:
            return 0

        n = len(prices)
        dp = [0] * n

        for i in range(n):
            # j goes from i to n
            for j in range(i, n):
                if prices[j] >= prices[i]:

                    dp[j] = max(dp[j], prices[j] - prices[i])


        return max(dp)


# Testing the function
solution = Solution()
print(solution.maxProfit([7,6,4,3,2,1]))

