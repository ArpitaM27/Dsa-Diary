class Solution(object):
    def isPalindrome(self, x):
        temp=x
        total=0
        if x<0:
            return False
            
        
        while temp!=0:
            digit=temp%10
            total=total*10+digit
            temp//=10
        
        if(total==x):
            return True
        else:
            return False