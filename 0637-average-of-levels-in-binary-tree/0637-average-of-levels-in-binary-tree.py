# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def averageOfLevels(self, root):
        if root is None:
            return []
        queue=deque([root])
        ans=[]
        while queue:
        
        
           level_size = len(queue)
           level=[]
           for i in range(level_size):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                     queue.append(node.left)
                if node.right:
                    queue.append(node.right)
           level = float(sum(level)) / len(level)
           ans.append(level)
        return ans

        