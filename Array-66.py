class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        for x in range(len(digits) - 1, -1, -1):
            if digits[x] == 9: # if our last digit is 9
                if len(digits) >= 2:
                    digits[x] = 0 # change last digit to 0
                    digits[x - 1] += 1 # add 1 to the prev index
                else:
                    digits[x] = 1
                    digits.append(0)
                return digits

            elif digits[x] < 9:
                digits[x] += 1
                return digits


solution_instance = Solution()
result = solution_instance.plusOne([9,9]) # 1 2 3 0
print(result)