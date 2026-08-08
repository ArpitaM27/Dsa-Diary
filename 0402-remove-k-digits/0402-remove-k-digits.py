class Solution(object):
    def removeKdigits(self, num, k):
        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        # If k is still left, remove from the end
        while k > 0:
            stack.pop()
            k -= 1

        # Build answer and remove leading zeros
        ans = "".join(stack).lstrip("0")

        return ans if ans else "0"