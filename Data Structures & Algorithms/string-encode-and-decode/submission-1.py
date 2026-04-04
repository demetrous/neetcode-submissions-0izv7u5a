class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word
        
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            str_len = ""
            while s[i] != "#":
                str_len += s[i]
                i += 1
            i += 1
            res.append(s[i: i + int(str_len)])
            i += int(str_len)
        
        return res
