class Solution:
    def minimumTotal(self, triangle):
        # Initialize a dp array with the values of the last row in the triangle
        dp = triangle[-1]

        # Iterate from the second-last row up to the first row
        for row in range(len(triangle) - 2, -1, -1):
            # Update dp array by storing minimum path sum for each position
            for col in range(len(triangle[row])):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])

        # The minimum path sum starting from the top will be in dp[0]
        return dp[0]


# Example usage
solution = Solution()
print(solution.minimumTotal([[-1], [2, 3], [1, -1, -3]]))

##
#   -1
#    2 3
#    1 -1 -3
