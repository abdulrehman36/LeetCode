
#
# isSub = { false <- if len(s) > len(t)
#           s(i+1), t(j+1) <- if match
#           s(i), t(j+1)   <- no match }


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)


solution = Solution()
print(solution.isSubsequence(["abc"],["ace"]))

# Notes
# n = len(s)
#         dp = [0] * len(t)
#         #dp[0] = s[0] # initializing table
#
#
#         if len(s) > len(t): # base case
#             return False
#         j = 0
#         for i in range(len(s[0])):
#             if s[0][i] == t[0][j]:
#                 dp[i] = t[0][i]
#             else:
#                 j += 1
#
#             if j == len(t[0]):
#                 return False

# i tried a dp solution but its easier to use pointers
# my entire idea of keeping track of indices is flawed.

# solution is as follows
# if the two letters match, increment i and j.
# if they dont match, increment j
# at the end, check if i == len(s) return true.
