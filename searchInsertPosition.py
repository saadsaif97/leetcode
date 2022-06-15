from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while(left <= right):
            mid = left + (right-left) // 2
            midValue = nums[mid]
            if(midValue == target):
                return mid
            if(target < midValue):
                right = mid-1
            if(midValue < target):
                left = mid+1
        return left


solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 2))
