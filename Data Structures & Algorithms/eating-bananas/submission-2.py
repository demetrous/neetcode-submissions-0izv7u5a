class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_speed = r 

        while l <= r:
            cur_speed = (l + r) // 2
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile/cur_speed)
            
            if total_time <= h:
                min_speed = cur_speed
                r = cur_speed - 1
            else:
                l = cur_speed + 1
        
        return min_speed
