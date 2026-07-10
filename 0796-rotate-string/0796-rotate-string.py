class Solution(object):
    def rotateString(self, s, goal):
        if len(s) !=len(goal):
            return False
        if s in goal+goal:
            return True
        return False
        