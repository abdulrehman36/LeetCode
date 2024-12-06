# Greedy 2144: Minimum cost of buying candies with Discount

# for every two candies sold, a third is free.

# any candy can be free but the choosen candy cost <= min(a, b) where a b are 2 of the
#candies we bought

# Input: [1,2,3]
# output: 5. Bought 2 and 3 and took 1 for free since 1 < min(2,3).

#Input: [6,5,7,9,2,2]
#output: 23. [0,2,5,0,7,9]. Buy 2 + 5 + 7 + 9 = 23

class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort() # sorting so for every 3 candies, the first one is free and we pay for other 2

        cost.reverse()

        if len(cost) < 3: # edge cast: less than 3 elements
            return sum(cost)

        i = 0
        for i in range(len(cost)):
            i += 1
            if i % 3 == 0:
                print("third item",i)


        return sum(cost)


solution = Solution()
print(solution.minimumCost([1,2,3]))


