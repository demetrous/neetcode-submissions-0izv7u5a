class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s + "|-|"      
        return res

    def decode(self, s: str) -> List[str]:
        i = j = 0
        res = []
        divider = "|-|"

        while i < len(s):          

            if i+2 < len(s) and s[i:i+3] == "|-|":
                res.append(s[j:i])
                i += 3                
                j = i     
                           
            else: i += 1     
        return res

            