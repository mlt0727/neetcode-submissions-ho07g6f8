class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                temp = min(height[i],height[j])*abs(j-i)
                if temp > answer:
                    answer = temp
        return answer