class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            cur_longest = 0
            if n - 1 not in numSet:
                cur_longest = 0
                while n + cur_longest in numSet:
                    cur_longest += 1
                longest = max(longest, cur_longest)
        
        return longest
