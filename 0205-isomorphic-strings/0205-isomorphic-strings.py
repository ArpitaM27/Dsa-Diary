class Solution(object):
    def isIsomorphic(self, s, t):

        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):

            # If mapping already exists, it must match
            if s[i] in s_to_t:
                if s_to_t[s[i]] != t[i]:
                    return False
            else:
                s_to_t[s[i]] = t[i]

            # Reverse mapping must also match
            if t[i] in t_to_s:
                if t_to_s[t[i]] != s[i]:
                    return False
            else:
                t_to_s[t[i]] = s[i]

        return True