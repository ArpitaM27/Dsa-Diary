class Solution(object):
    def reverseString(self, s):
        slow=0
        fast=len(s)-1
        while slow<fast:
            s[slow],s[fast]=s[fast],s[slow]
            slow+=1
            fast-=1
        return s