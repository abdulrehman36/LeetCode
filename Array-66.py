class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for x in range(len(digits) - 1, -1, -1):
            if digits[x] == 9:
                digits[x] = 0
            else:
                digits[x] += 1
                return digits

        digits.insert(0, 1)
        return digits


solution_instance = Solution()
result = solution_instance.plusOne([1,2,3,4])
print(result)  # Output: [1, 0, 0]