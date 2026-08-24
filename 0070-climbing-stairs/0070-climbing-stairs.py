class Solution(object):
    def climbStairs(self, n):
        memo = {}

        def solve(n):
            if n == 0:
                return 1

            if n == 1:
                return 1

            if n in memo:
                return memo[n]

            memo[n] = solve(n-1) + solve(n-2)

            return memo[n]

        return solve(n)