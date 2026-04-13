class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        answer = 0
        for i in s:
            if i in sub:
                answer = max(answer, len(sub))
                sub = sub[sub.index(i) + 1:]
                sub += i
            else:
                sub += i
        answer = max(answer, len(sub))
        return answer
            