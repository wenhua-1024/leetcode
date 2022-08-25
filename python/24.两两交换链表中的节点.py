#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        re_head = ListNode()
        re_head.next = head
        res = re_head
        while res is not None and res.next is not None and res.next.next is not None:
            
            tmp = res.next.next
            res.next.next = tmp.next
            tmp.next = res.next
            res.next = tmp
            
            res = res.next.next
        return re_head.next
# @lc code=end

if __name__ == "__main__":
    list_1 = ListNode(4)
    list_2 = ListNode(3, list_1)
    list_3 = ListNode(2, list_2)
    list_4 = ListNode(1, list_3)
    sol = Solution()
    res = sol.swapPairs(list_4)