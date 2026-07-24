class Solution(object):
    def plusOne(self, digits):
        x=int("".join(map(str,digits)))+1
        
        arr=[]
        for i in str(x):
            arr.append(int(i))
        return arr