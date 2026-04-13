class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height)
        left = 0
        right = len(height) - 1
        max_vol = 1
        while left <= right:
            if height[left] <= height[right]:
                vol = height[left] * (right - left)
                left += 1
            else:
                vol = height[right] * (right - left)
                right -= 1            
            if vol > max_vol:
                max_vol = vol
            
        return max_vol