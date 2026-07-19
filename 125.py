class Solution(object):
    def isan(self,s):
        a=""
        for i in s:
            if i.isalnum():
                a=a+i.lower()
        return a

    def isPalindrome(self, s):
        s=self.isan(s)
        r=s[::-1]
        if s==r:
            return True
        return False        
