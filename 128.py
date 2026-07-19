class Solution(object):
    def longestConsecutive(self, nums):
        n=len(nums)
        myset=set(nums)
        ans=0
        for num in myset:
            if num-1 not in myset:
                count=1
                x=num
                while num+1 in myset:
                    count+=1
                    num+=1
                ans=max(count,ans)
        return ans
