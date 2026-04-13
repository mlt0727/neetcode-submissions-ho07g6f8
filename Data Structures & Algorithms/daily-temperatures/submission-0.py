class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack1 = []

        for index, value in enumerate(temperatures):
            while stack1 and stack1[-1][0] < value:
                v, i = stack1.pop()
                answer[i] = index - i
            stack1.append((value, index))
        return(answer)
