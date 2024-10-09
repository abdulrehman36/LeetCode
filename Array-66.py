class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        for x in range(len(digits) - 1, -1, -1):
            if digits[x] >= 9:
                digits[x] = 0
                digits[x - 1] += 1
                return digits
            elif digits[x] < 9:
                digits[x] += 1
                return digits


solution_instance = Solution()
result = solution_instance.plusOne([9]) # 1 2 3 0
print(result)