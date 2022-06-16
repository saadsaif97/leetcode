from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = []
        squared.sort()
        return squared
        # sorted(list(map(lambda x: x*x,nums)))
        # sorted(n*n for n in nums)


solution = Solution()
print(solution.sortedSquares(nums=[-5, 1, 2, -3, -4]))
