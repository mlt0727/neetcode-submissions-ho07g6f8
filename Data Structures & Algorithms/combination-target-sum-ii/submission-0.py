class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        solutions=[]
        
        def dfs(start, path, remaining):
            if remaining==0:
                solutions.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                c=candidates[i]
                if c>remaining:
                    break
                elif i>start and c==candidates[i-1]:
                    continue
                else:
                    path.append(c)
                    dfs(i+1, path, remaining-c)
                    path.pop()
        dfs(0,[],target)
        return solutions