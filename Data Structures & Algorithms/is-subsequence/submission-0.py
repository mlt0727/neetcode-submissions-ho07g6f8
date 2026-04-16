class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        q = deque(s)
        for c in t:
            if q and c == q[0]:
                q.popleft()
        return True if not q else False