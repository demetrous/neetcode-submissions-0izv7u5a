class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(", "]":"[","}":"{"}
        stack = []

        for bracket in s:
            if bracket not in brackets:
                stack.append(bracket)
                continue

            if not stack or stack[-1] != brackets[bracket]:
                return False
            stack.pop()
        
        return not stack
