class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for c in tokens:
            if c in "+-*/":
                if c == "+":
                    a, b = int(stack.pop()), int(stack.pop())
                    stack.append(a + b)
                if c == "-":
                    a, b = int(stack.pop()), int(stack.pop())
                    stack.append(b - a)
                if c == "*":
                    a, b = int(stack.pop()), int(stack.pop())
                    stack.append(a * b)
                if c == "/":
                    a, b = int(stack.pop()), int(stack.pop())
                    stack.append(int(float(b) / a))
            else:
                stack.append(c)
        
        return int(stack[0])