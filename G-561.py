class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort() # sorting the list
        # Change every second number to 0. If we sort (a,b). min will be a.
        for i in range(1, len(nums), 2):
            nums[i] = 0

        return sum(nums) # gives the sum of the min pairs


solution = Solution()
print(solution.arrayPairSum([6,2,6,5,1,2]))


#O(nlogn) solution............. can possibly be O(n)