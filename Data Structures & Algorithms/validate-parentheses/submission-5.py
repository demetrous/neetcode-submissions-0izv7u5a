class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"}":"{", "]":"[", ")":"("}
        stack = []

        for brace in s:
            if brace not in pairs:
                stack.append(brace)
                continue

            if not stack or stack[-1] != pairs[brace]:
                return False
            stack.pop()

        return not stack