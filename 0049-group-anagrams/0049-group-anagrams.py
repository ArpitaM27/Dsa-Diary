from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for x in strs:
            s=sorted(x)
            key = "".join(s)
            d[key].append(x)
        return list(d.values())