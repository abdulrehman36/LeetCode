class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        # storing SP
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        # filling table based on the recurrence relation
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # The answer is stored in dp[n]
        return dp[n]


# Testing the function
solution = Solution()
print(solution.climbStairs(3))
