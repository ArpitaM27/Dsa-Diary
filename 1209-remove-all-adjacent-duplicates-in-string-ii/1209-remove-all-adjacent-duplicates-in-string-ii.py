class Solution(object):
    def removeDuplicates(self, s, k):
        stack = []

        for x in s:
            if not stack or x!=stack[-1][0]:
                stack.append([x, 1])
            else:
                stack[-1][1] += 1

            if stack[-1][1]==k:
                stack.pop()

        result = ""
        for char, freq in stack:
            result += char*freq

        return result