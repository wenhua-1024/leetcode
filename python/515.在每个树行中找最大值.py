#
# @lc app=leetcode.cn id=515 lang=python
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Queue import Queue
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res
        queue = Queue()
        queue.put(root)
        size = queue.qsize()
        while size != 0:
            max_res = float('-inf')
            for i in range(size):
                item = queue.get()
                max_res = max(max_res, item.val)
                if item.left is not None:
                    queue.put(item.left)
                if item.right is not None:
                    queue.put(item.right)
            size = queue.qsize()
            res.append(max_res)
        return res

        
# @lc code=end

