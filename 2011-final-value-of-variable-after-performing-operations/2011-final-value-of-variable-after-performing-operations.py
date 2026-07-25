class Solution(object):
    def finalValueAfterOperations(self, operations):
        val=0
        for x in operations:
            if x==("++X")or x== "X++":
                val=val+1
            if x==("--X") or x=="X--":
                val=val-1
        return val