
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
