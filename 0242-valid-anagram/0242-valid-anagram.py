class Solution(object):
    def isAnagram(self, s, t):
        d1={}
        d2={}
        for x in t:
                d1[x]=d1.get(x,0)+1
        for y in s:
                d2[y]=d2.get(y,0)+1
                
        return d1==d2