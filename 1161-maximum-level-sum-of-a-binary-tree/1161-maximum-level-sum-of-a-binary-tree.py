# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def maxLevelSum(self, root):

        if root is None:
            return 0

        queue = deque([root])

        level = 0
        max_sum = float('-inf')
        answer = 0

        while queue:

            level += 1
            level_sum = 0

            level_size = len(queue)

            for i in range(level_size):

                node = queue.popleft()

                level_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                answer = level

        return answer
        
        