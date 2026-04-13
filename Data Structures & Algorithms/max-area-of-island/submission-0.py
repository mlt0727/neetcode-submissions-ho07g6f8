class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set() #  存去过的
        maxisland = 0 

        def dfs(r, c):
            if (r,c) in visit or r not in range(rows) or c not in range(cols) or grid[r][c] == 0:
                return 0
            visit.add((r, c))
            return dfs(r+1, c) + dfs(r-1,c) + dfs(r, c+1) + dfs(r, c-1) + 1

        for r in range(rows):
            for c in range(cols):
                curmax = 0
                if grid[r][c] == 1:
                    curmax = dfs(r, c)
                maxisland = max(maxisland, curmax)
        return maxisland
                
