class Solution(object):
    def containsDuplicate(self, nums):
        n=len(nums)
        ans=set(nums)
        an=len(ans)
        if n==an:
            return False
        return True
