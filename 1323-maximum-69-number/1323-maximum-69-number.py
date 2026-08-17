class Solution(object):
    def maximum69Number (self, num):
        i=0
        num = list(str(num))
        while(i<len(num)):
            if num[i]=="6":
                num[i]="9"
                break
            i+=1
        return int("".join(num))

    