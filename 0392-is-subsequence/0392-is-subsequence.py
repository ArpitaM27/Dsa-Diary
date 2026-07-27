class Solution(object):
    def isSubsequence(self, s, t):
      a=0
      b=0
      if len(s)==0:
          return True
      while b < len(t):
          
          if s[a]==t[b]:
             
             if (a==(len(s)-1)):
                 return True
             a=a+1
             b=b+1
          else:
              b=b+1
      return False    
  