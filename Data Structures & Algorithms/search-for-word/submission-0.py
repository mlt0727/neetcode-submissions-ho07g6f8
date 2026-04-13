class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(x, y, path, visited):
            if len(path) > len(word):
                return False
            if len(path) == len(word):
                return True
            if x < 0 or y < 0 or x >= m or y >= n:
                return False
            if (x, y) in visited:
                return False
            if board[x][y] != word[len(path)]:
                return False
            
            visited.add((x, y))
            path += board[x][y]
            
            found = (
                dfs(x+1, y, path, visited) or
                dfs(x-1, y, path, visited) or
                dfs(x, y+1, path, visited) or
                dfs(x, y-1, path, visited)
            )
            
            visited.remove((x, y))
            return found
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, "", set()):
                    return True
        
        return False