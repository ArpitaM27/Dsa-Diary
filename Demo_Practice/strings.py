# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".



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