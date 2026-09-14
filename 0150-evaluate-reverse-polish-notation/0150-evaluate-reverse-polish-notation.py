class Solution(object):
    def evalRPN(self, tokens):
        stack=[]
        for ch in tokens:
            if ch not in ['+', '-', '*', '/']:
                stack.append(int(ch))
            else:
                a=stack.pop()
                b=stack.pop()
                if ch=='-':
                    result=b-a
                elif ch=='+':
                    result=b+a
                elif ch=='/':
                    result=int(float(b)/a)
                else:
                    result=b*a
                stack.append(result)
        return stack[0]

       