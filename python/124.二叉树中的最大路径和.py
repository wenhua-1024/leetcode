#
# @lc app=leetcode.cn id=124 lang=python
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    max_sum = -1001
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_sum = self.get_max_path_sum(root)
        return max(self.max_sum, max_sum)
    
    def get_max_path_sum(self, root):
        if root is None:
            return -1001
        left_max = self.get_max_path_sum(root.left)
        right_max = self.get_max_path_sum(root.right)
        max_sum = max([left_max, right_max, left_max + right_max + root.val, 
                        left_max + root.val, right_max + root.val])
        self.max_sum = max(max_sum, self.max_sum)

        return max(left_max + root.val, right_max + root.val, root.val)
        
# @lc code=end

