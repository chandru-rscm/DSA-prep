class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n==0:
            return 1
        total=10
        uniq=9
        avail=9
        for i in range(2,n+1):
            uniq*=avail
            total+=uniq
            avail-=1
        return total
