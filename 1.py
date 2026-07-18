class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        freq={}
        for i in range(n):
            rem=target-nums[i]
            if rem in freq:
                return [freq[rem],i]
            freq[nums[i]]=i
