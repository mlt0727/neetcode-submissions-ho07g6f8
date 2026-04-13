class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l = 0
        r = len(height) - 1
        lmax = 0
        rmax = 0
        water = 0
        i = l
        while l < r:
            water = min(rmax,lmax) - height[i]
            water = water if water > 0 else 0
            total += water
            lmax = max(height[l], lmax)
            rmax = max(height[r], rmax)
            if height[l] > height[r]:
                r -= 1
                i = r
            else:
                l += 1
                i = l
        return total

