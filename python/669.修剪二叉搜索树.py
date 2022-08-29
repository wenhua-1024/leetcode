#
# @lc app=leetcode.cn id=669 lang=python
#
# [669] 修剪二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        return self.get_trim(root, low, high)
        
    def get_trim(self, root, low, high):
        if root is None:
            return None
        if root.left is not None:
            root.left = self.get_trim(root.left, low, high)
        if root.right is not None:
            root.right = self.get_trim(root.right, low, high)

        if root is not None:
            if root.val >= low and root.val <= high:
                return root
        if root.left is not None:
            if root.left.val >= low and root.left.val <= high:
                return root.left
        if root.right is not None:
            if root.right.val >= low and root.right.val <= high:
                return root.right
        return None
# @lc code=end

