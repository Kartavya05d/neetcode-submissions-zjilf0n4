class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        while left <= right:
            speed = (left+right)//2
            hours_to_eat = 0 # number of banana / speed
            for pile in piles:
                hours_to_eat += math.ceil(pile/speed)
            if hours_to_eat <= h:
                res = min(res, speed)
                right = speed-1
            else:
                left = speed+1
        return res