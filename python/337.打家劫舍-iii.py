#
# @lc app=leetcode.cn id=337 lang=python
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        return int(max(self.get_tree_max(root)))
    def get_tree_max(self, root):
        # flag: 0表示不可以选根节点 1表示可以选根节点
        if root == None:
            return 0, 0
        # 偷取该节点
        left_steal, left_nosteal = self.get_tree_max(root.left)
        right_steal, right_nosteal = self.get_tree_max(root.right)

        # 偷取该节点
        steal = root.val + left_nosteal + right_nosteal
        
        # 不偷取该节点
        nosteal = max(left_steal, left_nosteal) + max(right_nosteal, right_steal)
        
        return steal, nosteal

# @lc code=end

