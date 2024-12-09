class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """

        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)

        maxUnit = 0
        i = 0
        while i < len(boxTypes) and truckSize > 0:
            numofbox, units = boxTypes[i]


            if numofbox <= truckSize:
                maxUnit += numofbox * units
                truckSize -= numofbox
            else:

                maxUnit += truckSize * units
                truckSize = 0  # Truck is full now

            i += 1

        return maxUnit


# my approach
# first sort the numberOfUnitsPerBox in increasing order.
# then run a while loop,
# if the numberofboxes <= truckisze
#     maxUnits += numofbox * units
#     trucksize -= numofboxes now we have to decrease the trucksize because we added boxes
# else: if our truckisze is less than the numofboxes in that subarray. take only what we can
#     maxUnit += truckSize * units
#     truckSize = 0  # Truck is full now

# running time: O(nlogn) <- because of the sorting step which made it easier because then we could consider boxtypes that had the highest numofunits



solution = Solution()
print(solution.maximumUnits([[1,3],[2,2],[3,1]], 1))