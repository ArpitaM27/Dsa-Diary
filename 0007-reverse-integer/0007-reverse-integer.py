class Solution(object):
    def reverse(self, x):
        total = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            total = total * 10 + digit
            x = x // 10

        if total > 2147483647:
            return 0

        return sign * total