#
# @lc app=leetcode.cn id=111 lang=python
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.bfs(root)
    def bfs(self, root):
        tmp = []
        tmp.append(root)
        depth = 0
        while(len(tmp) > 0):
            depth += 1
            length = len(tmp)
            for i in range(length):
                node = tmp.pop(0)
                if node.left is None and node.right is None:
                    return depth
                if node.left is not None:
                    tmp.append(node.left)
                if node.right is not None:
                    tmp.append(node.right)
        return depth
        
# @lc code=end

