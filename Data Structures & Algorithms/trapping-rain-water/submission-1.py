class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = l, r
        trapped = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] > height[l_max]:
                    l_max = l
                else:
                    trapped += height[l_max]- height[l]
                    l+= 1
            else:
                if height[r] > height[r_max]:
                    r_max = r
                else:
                    trapped += height[r_max] - height[r]
                    r -= 1

        return trapped 

