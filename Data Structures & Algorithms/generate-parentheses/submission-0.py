class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = ""
        def dfs(c,o,cur):
            if c == n and o == n:
                res.append(cur)
                return
            if o<=n:   
                dfs(c,o+1,cur + "(")
            if o>c:
                dfs(c+1,o,cur + ")")

        dfs(0,0,cur)
        return res