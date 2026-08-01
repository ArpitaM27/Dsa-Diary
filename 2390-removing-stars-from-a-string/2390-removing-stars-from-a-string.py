class Solution(object):
    def removeStars(self, s):
        stack=[]
        for x in s:
            if x!="*":
                stack.append(x)
            if x=="*":
                
                stack.pop()
        return "".join(stack)
    