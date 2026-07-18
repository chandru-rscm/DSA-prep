class Solution(object):
    def sortstr(self,stringg):
        an=list(stringg)
        an.sort()
        return "".join(an)

    def groupAnagrams(self, strs):
        n=len(strs)
        dict1={}
        for i in strs:
            an=self.sortstr(i)
            if an in dict1:
                dict1[an].append(i)
            else:
                dict1[an]=[i]
        return dict1.values()
        
        
