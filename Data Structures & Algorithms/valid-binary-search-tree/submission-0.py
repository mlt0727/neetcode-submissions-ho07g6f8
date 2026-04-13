# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, l, r):
            while not root:
                return True
            n = root.val
            if not (l < n < r):
                return False
            return dfs(root.left, l, n) and dfs(root.right, n, r)

        return dfs(root, float('-inf'), float('inf'))