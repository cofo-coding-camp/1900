# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.max = 0
        self.dfs(root)
        return self.max
    def dfs(self,root):
        if not root:
            return 0
        else:
            left_len = self.dfs(root.left)
            right_len = self.dfs(root.right)
            if root.left and root.left.val == root.val:
                left_len += 1
            else:
                left_len = 0
                
            if root.right and root.right.val == root.val:
                right_len += 1
            else:
                right_len = 0
            self.max = max(self.max, left_len+right_len)
            return max(left_len,right_len)
