class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Stack stores tuples of (start_index, height)
        stack = [] 
        max_area = 0

        for current_index, current_height in enumerate(heights):
            start_index = current_index
            
            # Maintain monotonic increasing stack
            while stack and stack[-1][1] > current_height:
                popped_index, popped_height = stack.pop()
                
                # Calculate width from the popped index to the current index
                width = current_index - popped_index
                max_area = max(max_area, width * popped_height)
                
                # The current bar can extend backwards to the popped index
                start_index = popped_index
            
            stack.append((start_index, current_height))
        
        # Process remaining items in the stack
        # These extend to the very end of the heights array
        total_width = len(heights)
        for start_index, height in stack:
            width = total_width - start_index
            max_area = max(max_area, width * height)
        
        return max_area