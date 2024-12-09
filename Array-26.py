


#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

#Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

#Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
# The remaining elements of nums are not important as well as the size of nums.
#Return k


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Pointer for the position of the last unique element
        unique_pos = 0

        # Loop through the array starting from the second element
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_pos]:
                unique_pos += 1
                nums[unique_pos] = nums[i]

        # Trim the list to contain only unique elements
        del nums[unique_pos + 1:]

        return unique_pos + 1  # Length of the list with unique elements


# Usage example
solution = Solution()
nums = [1, 1, 1, 2]
length = solution.removeDuplicates(nums)
print(f"Array after removing duplicates: {nums}")
print(f"Length of unique array: {length}")


