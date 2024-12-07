# DP 198 House robbers

#


class Solution(object):
    def rob(self, nums):

        # Check if the input list is empty
        if not nums:
            return 0

        # Handle the base cases when there are only one or two houses
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # Initialize an array to store the maximum amount of money robbed up to each house
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Iterate through the houses, calculating the maximum amount of money robbed up to each house
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        # Return the maximum amount of money robbed from all houses
        return dp[-1]

solution = Solution()
print(solution.rob([1,2,3,1]))

