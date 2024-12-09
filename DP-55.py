class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == 1:
            return True

        n = len(nums)
        # initializing the table
        dp = [True for i in range(n)]

        for i in range(n-2,-1,-1):
            if nums[i] <= nums[i + 1]:  # take jump
                dp[i] = True



        print(dp)


solution = Solution()
print(solution.canJump([1,0,3]))