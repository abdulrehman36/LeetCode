class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):  # Loop through the list
            if nums[i] != val:
                k += 1  # Count the elements not equal to val

        i = 0  # Reset i for the while loop
        last_index = len(nums) - 1

        while i < last_index:
            if nums[i] == val:
                nums[i], nums[last_index] = nums[last_index], nums[i]  # Swap
                last_index -= 1  # Decrease last_index
            else:
                i += 1  # Increment i when no swap is made

        return nums


# Create an instance of the Solution class
solution = Solution()

# Define the list and the value to remove
nums = [3, 2, 2, 3]
val = 3

# Call the removeElement method and print the result
result = solution.removeElement(nums, val)
print(result)  # Output will be the count of elements not equal to val

