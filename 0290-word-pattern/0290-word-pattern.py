class Solution(object):
    def wordPattern(self, pattern, s):
        d1 = {}
        d2 = {}
        s = s.split()

        if len(pattern) != len(s):
            return False

        for i in range(len(pattern)):

            if pattern[i] in d1:
                if d1[pattern[i]] != s[i]:
                    return False
            else:
                d1[pattern[i]] = s[i]

            if s[i] in d2:
                if d2[s[i]] != pattern[i]:
                    return False
            else:
                d2[s[i]] = pattern[i]

        return True