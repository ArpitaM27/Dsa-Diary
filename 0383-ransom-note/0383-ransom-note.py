class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        d1={}
        d2={}
        for x in ransomNote:
            d1[x]=d1.get(x,0)+1
        for x in magazine:
            d2[x]=d2.get(x,0)+1
        for ch in d1:
            if d1.get(ch,0)>d2.get(ch,0):
                return False
        return True
