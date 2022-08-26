#
# @lc app=leetcode.cn id=104 lang=python
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    max_depth = 0
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is not None:
            self.get_max_depth(root, 1)
        return self.max_depth
    
    def get_max_depth(self, root, count):
        if count > self.max_depth:
            self.max_depth = count
        if root.left is not None:
            self.get_max_depth(root.left, count+1)
        if root.right is not None:
            self.get_max_depth(root.right, count+1)
        return

        
# @lc code=end

