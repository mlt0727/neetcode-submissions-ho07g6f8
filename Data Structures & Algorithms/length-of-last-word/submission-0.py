class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        count = 0
        for i in s.strip():
            if i == " ":
                ans = count
                count = 0
                continue
            count += 1
        ans = count
        return ans