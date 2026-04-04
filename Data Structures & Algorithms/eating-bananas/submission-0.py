class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = r = max(piles)
        l = 1

        while l <= r:
            mid = (l + r) // 2
            time = 0
            for pile in piles:
                time += math.ceil(float(pile)/mid)
            if time <= h:
                min_speed = mid
                r = mid - 1
            else:
                l = mid + 1
                
        return min_speed