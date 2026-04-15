class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        q = deque()
        q.appendleft(-1)
        maxn = arr[-1]
        for i in range(len(arr)-2,-1,-1):
            q.appendleft(maxn)
            maxn = max(maxn, arr[i])
        return list(q)
