class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                cur_longest = 1
                while num + cur_longest in numSet:
                    cur_longest += 1
                longest = max(longest, cur_longest)
        
        return longest