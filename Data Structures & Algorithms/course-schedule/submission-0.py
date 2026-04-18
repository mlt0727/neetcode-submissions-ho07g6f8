class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = defaultdict(set)
        for pre in prerequisites:
            premap[pre[0]].add(pre[1])
        
        def dfs(num, visit):
            if not premap[num]:
                return True
            if num in visit:
                return False
            else:
                visit.add(num)
            check = True
            for n in premap[num]:
                check = check and dfs(n, visit)
            visit.remove(num)
            if check:
                premap[num] = set()
                return True
            else:
                return False
        
        ans = True
        for c in range(numCourses):
            ans = ans and dfs(c, set()) 
        return ans