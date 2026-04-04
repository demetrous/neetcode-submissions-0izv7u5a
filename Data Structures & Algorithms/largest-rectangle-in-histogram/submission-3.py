class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for current_index, current_height in enumerate(heights):
            start_index = current_index
            while stack and stack[-1][1] > current_height:
                popped_index, popped_height = stack.pop()
                max_area = max(max_area, popped_height * (current_index - popped_index))
                start_index = popped_index
            stack.append((start_index, current_height))
        
        for start_index, height in stack:
            max_area = max(max_area, height * (len(heights) - start_index))

        return max_area