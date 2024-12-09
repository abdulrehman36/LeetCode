class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        #   Base Case
        if len(cost) == 1:
            return cost[0]

        n = len(cost)
        dp = [0] * n
        dp[-1] = cost[-1] # initializing table
        dp[-2] = cost[-2]

        for step in range(n-3,-1,-1):
            dp[step] = cost[step] + min(dp[step+1],dp[step+2]) # main step

        return min(dp[0],dp[1])


solution = Solution()
print(solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))







#
#
#   minCostClimbingStairs(cost) =  {
#                                   cost[0] <- if cost.length = 1
#                                   dp[i] = cost[i] + min(dp[i+1],dp[i+2]) <- otherwise
#







