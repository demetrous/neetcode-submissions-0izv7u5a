class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, r = 0, 0
        longest = 0

        while r < len(s):
            if charSet and s[r] in charSet:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
            charSet.add(s[r])
            r += 1
            longest = max(longest, r - l)
        
        return longest
