class Solution(object):
    def arrayRankTransform(self, arr):
        dict1={}
        rank=1
        for i in sorted(arr):
            if i not in dict1:
                dict1[i]=rank
                rank+=1
        ans=[]
        for i in arr:
            ans.append(dict1[i])
        return ans

        
