# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.ans = True
        def dfs(p,q):
            if not p or not q:
                if not(not p and not q):
                    self.ans = False
                return None

            if p.val != q.val:
                self.ans = False

            dfs(p.left, q.left)
            dfs(p.right, q.right)
            
        dfs(p,q)
        return self.ans
