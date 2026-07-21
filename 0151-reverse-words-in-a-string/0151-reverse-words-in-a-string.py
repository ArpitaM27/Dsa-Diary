class Solution(object):
    def reverseWords(self, s):
          s=s.split()
          slow=0
          fast=len(s)-1
          while slow<fast:
            s[slow],s[fast]=s[fast],s[slow]
            slow+=1
            fast-=1
          s=" ".join(s)
          return s