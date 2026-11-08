class Solution(object):
    def minSwaps(self, s):
        balance = 0
        imbalance=0

        for x in s:
            if x == '[':
                    balance += 1
            else:
                    balance -= 1
            if balance<0:
                imbalance=max(imbalance,abs(balance))
            swap=(imbalance+1)//2
        return swap
             

        
                    