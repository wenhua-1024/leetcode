#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()
        res = ListNode()
        head = res
        l1_tmp = l1
        l2_tmp = l2
        flag = 0
        while(l1_tmp is not None or l2_tmp is not None or flag > 0):
            tmp = ListNode(val=flag)
            if l1_tmp is not None:
                tmp.val += l1_tmp.val
                l1_tmp = l1_tmp.next
            if l2_tmp is not None:
                tmp.val += l2_tmp.val
                l2_tmp = l2_tmp.next
            if tmp.val >= 10:
                tmp.val %= 10
                flag = 1
            else:
                flag = 0
            res.next = tmp
            res = res.next
        return head.next

# @lc code=end

