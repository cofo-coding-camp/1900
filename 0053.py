class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        maxSum = nums[0]
        for i in nums:
            
            if currentSum < 0:
                currentSum = i
            else:
                currentSum += i
            maxSum = max(currentSum,maxSum)
            
        return maxSum
            
