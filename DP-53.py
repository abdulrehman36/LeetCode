class Solution(object):
    def maxSubArray(self, nums):
        """
        :rtype: int
        """
        # base case
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0] # initializing table

        for i in range(n):
            dp[i] = max((nums[i]),(dp[i-1] + nums[i]))


        return max(dp)


# Testing the function
solution = Solution()
print(solution.maxSubArray([0]))