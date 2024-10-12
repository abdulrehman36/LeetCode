#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums) - 1):
            for x in range(i+1,len(nums)):
                if nums[i] == nums[x]:
                    return True

        return False


solution_instance = Solution()
result = solution_instance.containsDuplicate([1,2,3,4,5])

print(result)