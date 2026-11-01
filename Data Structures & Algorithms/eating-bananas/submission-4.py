class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        hr = right

        while left <= right:
            ban_per_hr = left + (right-left)//2
            hrs_to_eat = 0
            for pile in piles:
                hrs_to_eat += math.ceil(pile/ban_per_hr)

            if hrs_to_eat <= h:
                hr = min(hr, ban_per_hr)
                right = ban_per_hr-1
            else:
                left = ban_per_hr+1
        return hr
