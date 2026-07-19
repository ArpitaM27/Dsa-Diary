class Solution(object):
    def firstUniqChar(self, s):
        d={}
        for x in s:
            d[x]=d.get(x,0)+1
    
        for i in range(len(s)):
            if d[s[i]]==1:
              return i
        return -1