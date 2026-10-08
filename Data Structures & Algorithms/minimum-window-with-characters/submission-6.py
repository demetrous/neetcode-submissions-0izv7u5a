class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        t_count = {}
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        
        window = {}
        have, need = 0, len(t_count) # <need> is how many unique chars in t
        res_len = float('inf') # initial min len of substring, the biggest number
        res = [-1,-1] # left and right boundaries of min substring in s
        l = 0

        for r in range(len(s)):
            c = s[r]

            window[c] = 1 + window.get(c, 0)
            
            if c in t_count and window[c] == t_count[c]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res_len = (r - l + 1)
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1

        return s[res[0]:res[1] + 1] if res_len < float('inf') else ""         

