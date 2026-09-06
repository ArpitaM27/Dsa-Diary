# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def largestValues(self, root):
        if root is None:
            return []

        queue = deque([root])
        ans = []

        while queue:
            size = len(queue)
            maximum = float('-inf')

            for i in range(size):
                node = queue.popleft()

                maximum = max(maximum, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            ans.append(maximum)

        return ans

