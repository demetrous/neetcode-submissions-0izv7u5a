class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = l

        while l <= r:
            mid = (l + r) // 2
            value = mid * mid
            if value <= x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return res