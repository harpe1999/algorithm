# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        res=[]
        if root is None:
            return res
        s=[]
        s.append(root)
        while len(s)>0:
            p=s.pop()
            res.append(p.val)
            if p.left is not None:
                s.append(p.left)
            if p.right is not None:
                s.append(p.right)
        res.reverse()
        return res
        
