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





<<<<<<< HEAD
=======
solution_instance = Solution()

>>>>>>> 87e7b06591c9a5a10920a40a45e75f1f10befcd8
result = solution_instance.plusOne([9]) # 1 2 3 0
print(result)