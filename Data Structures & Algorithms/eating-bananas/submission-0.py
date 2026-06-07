class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            mid = l + (r - l) // 2  # use integer division
            total_hour = 0

            for p in piles:
                total_hour += math.ceil(p / mid)  # no need to convert to float

            if total_hour <= h:
                ans = mid
                r = mid - 1  # fix variable name: high → r
            else:
                l = mid + 1  # fix variable name: low → l

        return ans 
        