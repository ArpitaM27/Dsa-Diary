class Solution(object):
    def calPoints(self, operations):
        stack=[]
        for x in operations:
            if stack and x=="C":
                stack.pop()
                continue
            if stack and x=="D":
                y=stack[-1]
                stack.append(2*y)
                continue
            if stack and x=="+":
                y=int(stack[-2])
                z=int(stack[-1])
                k=y+z
                stack.append(k)
                continue
            else:
                stack.append(int(x))
                continue
       
        return sum(stack)