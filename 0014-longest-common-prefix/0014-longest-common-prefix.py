class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            for string in strs:
                if string[i] != shortest[i]:
                    if i == 0:
                        return ""
                    return shortest[:i]

        return shortest
           