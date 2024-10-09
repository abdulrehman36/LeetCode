#   Palindrom Number
# Example
# input x = 121, output true.


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = str(x)[::-1]
        if (str(x) == reverse):
            return True
        return False



solution_instance = Solution()
result = solution_instance.isPalindrome(31)

print(result)