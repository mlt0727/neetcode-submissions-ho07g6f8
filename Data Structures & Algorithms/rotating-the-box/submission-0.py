class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows, cols = len(boxGrid), len(boxGrid[0])

        for r in range(rows):
            i = cols-1
            for c in range(cols-1,-1,-1):
                if boxGrid[r][c] == "*":
                    i = c - 1
                elif boxGrid[r][c] == "#":
                    boxGrid[r][c] = "."
                    boxGrid[r][i] = "#"
                    i -= 1
        
        ans = [[] for _ in range(cols)]
        for c in range(cols):
            for r in range(rows-1,-1,-1):
                ans[c].append(boxGrid[r][c])
        return ans

