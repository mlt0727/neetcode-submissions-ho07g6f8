from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        left = 1
        right = res
        while left <= right:
            temp = 0
            mid = (left + right) // 2
            for pile in piles:
                temp += ceil(pile/mid)
            if temp > h:
                left = mid + 1
            else:
                res = min(mid, res)
                right = mid - 1
        return res