class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1count = {}
        s2count = {}
        for i in range(len(s1)):
            s1count[s1[i]] = s1count.get(s1[i], 0) + 1
            s2count[s2[i]] = s2count.get(s2[i], 0) + 1

        for j, v in s1count.items():
            if s2count.get(j, 0) != v:
                break
        else:
            return True
        
        for i in range(len(s1), len(s2)):
            s2count[s2[i]] = s2count.get(s2[i], 0) + 1
            s2count[s2[i-len(s1)]] -= 1

            for j, v in s1count.items():
                if s2count.get(j, 0) != v:
                    break
            else:
                return True
        return False
