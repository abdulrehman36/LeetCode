class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSort = sorted(nums)

        left = 0
        while left < len(nums) and nums[left] == numsSort[left]:
            left += 1

        if left == len(nums):
            return 0

        right = len(nums) - 1
        while right >= 0 and nums[right] == numsSort[right]:
            right -= 1

        return right - left + 1

solution = Solution()
print(solution.findUnsortedSubarray([2,6,4,8,10,9,15]))

# solution
# first sory the array in increasing order
# Loop from the beginning, when we meet in index thats not the same in original array, store
# Loop from the end, when we meet in index thats not the same in original array, store
#
# return the difference between those arrays + 1 because indexing starts at 0

# running time: O(nlogn), because of the sorting step./