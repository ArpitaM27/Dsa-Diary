from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for x in range(int(sqrt(c))+1):
            b=sqrt(c-x*x)
            if b==int(b):
                return True
        return False
        