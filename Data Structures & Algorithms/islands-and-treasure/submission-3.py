class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r, c))
        d = 0
        dir = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                grid[r][c] = d
                for mr, mc in dir:
                    nr, nc = r+mr, c+mc
                    if (nr, nc) not in visit and nr >= 0 and nc >= 0 and nr < rows and nc < cols and grid[nr][nc] != -1:
                        q.append((nr,nc))
                        visit.add((nr, nc))
            d += 1
