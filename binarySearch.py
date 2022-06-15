from math import floor
from turtle import left
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_idx = 0
        right_idx = len(nums) - 1

        while(left_idx <= right_idx):
            midPoint = (left_idx+right_idx)//2
            midValue = nums[midPoint]

            if(target == midValue):
                return midPoint
            if(left_idx == right_idx and midValue != target):
                return -1

            if(target < midValue):
                right_idx = midPoint-1
            if(target > midValue):
                left_idx = midPoint+1

        return -1


solution = Solution()
print(solution.search(nums=[2, 5], target=0))
# print(solution.search(nums=[1, 2, 3, 4, 5, 6, 7], target=7))
# print(solution.search(nums=[1, 2, 3, 4, 5, 6, 7], target=3))
# print(solution.search(nums=[1, 2, 3, 4, 5, 6, 7], target=8))
# print(solution.search(nums=[1, 2, 3, 4, 5, 6, 7], target=1))


"""
Constraints:
• 1 <= nums.length <= 104
• -104 < nums[i], target < 104
• All the integers in nums are unique.
• nums is sorted in ascending order.
"""
