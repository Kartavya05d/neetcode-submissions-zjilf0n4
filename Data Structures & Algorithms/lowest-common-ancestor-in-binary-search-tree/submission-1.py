# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            #Both p and q belongs to same direction.
            curr_val = curr.val
            if p.val > curr_val and q.val > curr_val: curr = curr.right
            elif p.val < curr_val and q.val < curr_val: curr = curr.left
            #If it splits, current node is the LCA.
            else: return curr
