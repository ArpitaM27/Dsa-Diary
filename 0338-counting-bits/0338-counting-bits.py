class Solution(object):
    def countBits(self, n):
        arr=[0]* (n+1)
        
        for i in range(0,n+1,1):
            sum=0
            j=i
            while j:
                j=(j&(j-1))
                sum+=1
            arr[i]=sum
        return arr
         
      
        