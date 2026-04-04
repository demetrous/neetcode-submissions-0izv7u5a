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
            j = i
            while s[j] != "#":
                j += 1            
            word_length = int(s[i:j])
            j += 1
            res.append(s[j: j + word_length])
            i = j + word_length
        
        return res
