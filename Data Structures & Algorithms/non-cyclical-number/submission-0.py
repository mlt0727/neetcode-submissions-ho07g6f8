class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        res = n
        while res != 1:
            n = str(res)
            res = 0
            for num in n:
                res += int(num) ** 2
            if res in seen:
                return False
            else:
                seen.add(res)
        return True
