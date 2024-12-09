class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        N=1
        ans=0
        while word * N in sequence:
            ans = ans+1
            N = N+1
        return ans


solution = Solution()
print(solution.maxRepeating("ababc","ab"))