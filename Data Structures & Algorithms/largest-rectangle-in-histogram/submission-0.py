class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [index, height]
        largest = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                i_stack, h_stack = stack.pop()
                largest = max(largest, (i - i_stack) * h_stack)
                start = i_stack
            stack.append([start, h])
        
        for i in range(len(stack)):
            largest = max(largest, (len(heights) - stack[i][0]) * stack[i][1])
        
        return largest
