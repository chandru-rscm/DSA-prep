class Solution(object):
    def isAnagram(self, s, t):
        n=len(s)
        m=len(t)
        na=[]
        ma=[]
        if n!=m:
            return False
        for i in range(n):
            na.append(s[i])
            ma.append(t[i])
        na.sort()
        ma.sort()
        if na==ma:
            return True
        return False
      
