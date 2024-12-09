#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sorted = nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

solution_instance = Solution()
result = solution_instance.containsDuplicate([1,2,3,4,5,1])

print(result)