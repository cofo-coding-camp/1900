class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        self.nums = nums
        return self.construct(0,len(nums)-1)
    
    def construct(self,l,r):
        if l <= r:
            m = self.max_index(l,r)
            root = TreeNode(self.nums[m])
            root.left = self.construct(l,m-1)
            root.right = self.construct(m+1,r)
            return root
        
    def max_index(self,l,r):
        index = l
        for i in range(l,r+1):
            if self.nums[index] < self.nums[i]:
                index = i
        return index
