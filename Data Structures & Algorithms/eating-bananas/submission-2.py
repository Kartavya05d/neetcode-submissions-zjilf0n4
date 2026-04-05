class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        while left <= right:
            bananas_per_hour = (left + right) // 2
            hours_to_eat = 0
            for pile in piles:
                hours_to_eat += math.ceil(pile/bananas_per_hour)
            if hours_to_eat <= h:
                res = min(bananas_per_hour, res)
                right = bananas_per_hour -1
            else:
                left = bananas_per_hour + 1
        return res