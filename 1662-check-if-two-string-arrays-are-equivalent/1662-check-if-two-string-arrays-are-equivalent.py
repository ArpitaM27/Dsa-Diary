
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        arr="".join(word1)
        arr1="".join(word2)
        if arr==arr1:
            return True
        else:
            return False
        