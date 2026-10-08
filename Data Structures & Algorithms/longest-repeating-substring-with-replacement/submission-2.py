class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxFreq = output = 0
        freq = {}

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxFreq = max(maxFreq, freq[s[r]])

            if (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1

            output = max(output, r - l + 1)
        
        return output
