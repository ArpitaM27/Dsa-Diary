# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        val=preorder[0]
        root=TreeNode(val)
        mid=inorder.index(val)
        root.left=self.buildTree(
            preorder[1:1+mid],
            inorder[:mid]
         )
        root.right=self.buildTree(
            preorder[1+mid:],
            inorder[1+mid:]
         )
        return root
