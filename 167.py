class Solution(object):
    def twoSum(self, numbers, target):
        n=len(numbers)
        dict1={}
        for i in range(n):
            rem=target-numbers[i]
            if rem in dict1:
                return sorted([i+1,dict1[rem]+1])
            else:
                dict1[numbers[i]]=i
