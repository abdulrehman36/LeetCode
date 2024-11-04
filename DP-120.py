class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        dp = []

        for row in triangle:
            min_value = min(row)
            dp.append(min_value)

        return sum(dp)


solution = Solution()
print(solution.minimumTotal([[-1],[2,3],[1,-1,-3]]))

##
#   -1
#    2 3
#    1 -1 -3
