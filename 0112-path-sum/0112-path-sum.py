# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        
        def check(Node,sum):
            if not Node:
                return False
            sum+=Node.val
            if not Node.left and not Node.right:
                return sum==targetSum
            return (check(Node.left,sum) or check(Node.right,sum))
        return check(root,0)

            