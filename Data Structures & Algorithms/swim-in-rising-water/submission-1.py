class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minheap = [(grid[0][0],0,0)]
        visited = set()
        visited.add((0,0))
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minheap:
            val, r, c = heapq.heappop(minheap)
            if r == n - 1 and c == n - 1:
                return val
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    nval = max(val, grid[nr][nc])
                    heapq.heappush(minheap, (nval, nr, nc))