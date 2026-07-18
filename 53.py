class Solution(object):
    def maxSubArray(self, nums):
        ans=float('-inf')
        n=len(nums)
        summ=0
        for i in range(n):
            summ+=nums[i]
            if summ>ans:
                ans=summ
            if summ<0:
                summ=0
            
        return ans
