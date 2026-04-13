# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(root, n):
            if not root:
                return None
            if root.val >= n:
                n = root.val
                self.ans += 1
            
            dfs(root.left, n)
            dfs(root.right, n)
        
        dfs(root, root.val)
        return self.ans