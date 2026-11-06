class Solution(object):
    def numPairsDivisibleBy60(self, time):
        h={}
        count=0
        for x in time:
            r=x%60
            complement = (60 - r) % 60
            count+=h.get(complement,0)
            h[r]=h.get(r,0)+1
        return count
        