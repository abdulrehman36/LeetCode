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

        # Create a DP array to store the results of subproblems
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        # Fill the DP array based on the recurrence relation
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # The answer is stored in dp[n]
        return dp[n]


# Testing the function
solution = Solution()
print(solution.climbStairs(5))  # Change 5 to any number you want to test


