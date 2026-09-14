class Solution(object):
    def passwordStrength(self, password):

        count = 0
        seen = set()

        for ch in password:

            if ch in seen:
                continue

            if 'a' <= ch <= 'z':
                count += 1

            elif 'A' <= ch <= 'Z':
                count += 2

            elif '0' <= ch <= '9':
                count += 3

            elif ch in {'!', '@', '#', '$'}:
                count += 5

            seen.add(ch)

        return count