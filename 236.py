class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q 
        self.ans = None
        self.dfs(root)
        return self.ans
    def dfs(self, root):
        if root:
            mid = 0
            if root ==self.p or root == self.q:
                mid = 1
          
            left = 1 if self.dfs(root.left) else 0
            right = 1 if self.dfs(root.right) else 0
            if mid + right + left >= 2:
                self.ans = root

            return mid + left + right > 0

