
from math import factorial
class Solution(object):
    def trailingZeroes(self, n):
        x=factorial(n)
        count=0
        x=str(x)
        i=len(x)-1
        while x[i]=='0':
            count+=1
            i=i-1
            
    
        return count
    
        