class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for num in nums:
            if num - 1 not in numSet:
                cur_longest = 1
                while num + cur_longest in numSet:
                    cur_longest += 1
                longest = max(longest, cur_longest)
        
        return longest