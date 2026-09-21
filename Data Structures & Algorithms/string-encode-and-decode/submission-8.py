class Solution:
    def encode(self, strs: List[str]) -> str:
        # Using a list comprehension + join is O(n) and very fast
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = s.find("#", i) # A bit cleaner than a manual while loop
            word_length = int(s[i:j])
            i = j + 1
            res.append(s[i : i + word_length])
            i += word_length
        return res