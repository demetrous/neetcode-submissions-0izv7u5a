class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"]":"[", "}":"{",")":"("}
        stack = []

        for b in s:
            if b not in brackets:
                stack.append(b)
                continue
            if not stack or brackets[b] != stack[-1]:
                return False
            stack.pop()
        return not stack