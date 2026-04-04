class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            value = nums[mid]
            if value == target:
                return mid
            elif value > target:
                r = mid - 1
            else:
                l = mid + 1
        return l