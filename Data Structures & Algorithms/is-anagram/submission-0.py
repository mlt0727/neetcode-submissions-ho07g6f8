class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = {}
        hasht = {}
        n = len(s)
        if n != len(t):
            return False
        for i in range(n):
            hashs[s[i]] = 1 + hashs.get(s[i], 0)
            hasht[t[i]] = 1 + hasht.get(t[i], 0)
        for c in hashs:
            if hashs[c] != hasht.get(c, 0):
                return False
        return True 