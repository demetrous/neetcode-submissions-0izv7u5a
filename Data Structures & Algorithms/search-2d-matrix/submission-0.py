class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            middle = (left + right) // 2
            current_row = middle // cols
            current_col = middle % cols
            current_value = matrix[current_row][current_col]
            if current_value < target:
                left = middle + 1
            elif current_value > target:
                right = middle - 1
            else:
                return True
        
        return False