class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        checkerboard = [-1] * n
        cols = set()
        diag1 = set()
        diag2 = set()

        def is_safe(r, c):
            return c not in cols and (r-c) not in diag1 and (r+c) not in diag2

        def dfs(r, c, n):
            if r == n:
                res.append(checkerboard[:])
                return
            
            for col in range(c, n):
                if is_safe(r, col):
                    checkerboard[r] = col
                    cols.add(col)
                    diag1.add(r - col)
                    diag2.add(r + col)
                
                    dfs(r + 1, 0, n)

                    checkerboard[r] = -1
                    cols.remove(col)
                    diag1.remove(r - col)
                    diag2.remove(r + col)
        
        dfs(0, 0, n)

        solution = []
        for pos in res:
            board = []
            for col in pos:
                board.append("."*col + "Q" + "."*(n - 1 - col))
            solution.append(board)
        return solution
