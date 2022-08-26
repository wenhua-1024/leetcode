#
# @lc app=leetcode.cn id=160 lang=python
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA = headA
        pB = headB
        while True:
            if pA == pB:
                return pA
            pA = pA.next
            pB = pB.next
            if pA is None and pB is None:
                break
            if pA is None:
                pA = headB
            if pB is None:
                pB = headA
        return None
            
 
# @lc code=end

