class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s        
        return res


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            count_str = ""
            while s[i] != "#" and i < len(s):
                count_str += s[i]
                i += 1
            i += 1
            count = int(count_str)
            res.append(s[i:i + count])
            i += count
        
        return res