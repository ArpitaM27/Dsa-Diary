
class Solution(object):
    def nextno(self,n):
        total=0
        while n>0:
            
            digit=n%10
            total=total+digit*digit
            n=n//10
        return total
    
    def isHappy(self, n):
        slow=n
        fast=n
        while True:
             slow=self.nextno(slow)
             fast=self.nextno(self.nextno(fast))
             if (slow==1 or fast==1):
                 return True
             if(slow==fast):
                  return False
         