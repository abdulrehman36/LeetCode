from collections import Counter

class Solution(object):
    def minDominoRotations(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: int
        """
        def count_swaps(top, bottom):
            """
            Helper function to calculate the minimum swaps needed to align `top`
            with the most occurring value in `top`.
            """
            count_top = Counter(top)
            most_occurring = count_top.most_common(1)[0][0]
            swap_count = 0

            for i in range(len(top)):
                if top[i] != most_occurring:
                    if bottom[i] == most_occurring:
                        # Swap to make top[i] match most_occurring
                        top[i], bottom[i] = bottom[i], top[i]
                        swap_count += 1
                    else:
                        # If neither matches, alignment is impossible
                        return float('inf')

            # Verify if the alignment is complete
            if swap_count + count_top[most_occurring] == len(top):
                return swap_count
            else:
                return float('inf')

        # Try both possibilities
        swaps_a = count_swaps(a[:], b[:])  # Treat `a` as the top array
        swaps_b = count_swaps(b[:], a[:])  # Treat `b` as the top array

        # Get the minimum swaps required, or return -1 if impossible
        result = min(swaps_a, swaps_b)
        return result if result != float('inf') else -1

solution = Solution()
print(solution.minDominoRotations([1, 2, 1, 1, 1, 2, 2, 2], [2, 1, 2, 2, 2, 2, 2, 2]))

# O(n) run time but bad space complexity