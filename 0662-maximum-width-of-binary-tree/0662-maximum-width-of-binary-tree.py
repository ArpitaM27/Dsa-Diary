# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def widthOfBinaryTree(self, root):

        if root is None:
            return 0

        queue = deque([(root, 0)])
        ans = 0

        while queue:

            size = len(queue)
            first = queue[0][1]

            for i in range(size):

                node, index = queue.popleft()

                if node.left:
                    queue.append((node.left, 2 * index + 1))

                if node.right:
                    queue.append((node.right, 2 * index + 2))

            width = index - first + 1
            ans = max(ans, width)

        return ans

