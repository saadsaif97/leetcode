from tracemalloc import start
from turtle import right
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1 or k == 0:
            return

        window = len(nums) - (k % len(nums))
        nums[:] = nums[window:] + nums[:window]

        # for i, num in enumerate(nums[window:] + nums[:window]):
        #     nums[i] = num

        print(nums)


sol = Solution()
sol.rotate(nums=[1, 2, 3, 4], k=3)  # [2, 3, 4, 1]
