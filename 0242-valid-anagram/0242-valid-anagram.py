class Solution(object):
    def isAnagram(self, s, t):
        d1={}
        d2={}
        for x in t:
            if x in d1:
                d1[x]+=1
            else:
                d1[x]=1
        for y in s:
            if y in d2:
                d2[y]+=1
            else:
                d2[y]=1
        return d1==d2