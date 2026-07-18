class Solution(object):
    def topKFrequent(self, nums, k):
        dict1={}
        for i in nums:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        ans=[]
        for i in range(k):
            mx=max(dict1,key=dict1.get)
            ans.append(mx)
            dict1[mx]=0
        return ans
