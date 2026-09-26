class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_volume = 0

        while l < r:
            cur_volume = (r - l) * min(heights[l], heights[r])
            max_volume = max(max_volume, cur_volume)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_volume