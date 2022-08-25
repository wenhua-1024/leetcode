#
# @lc app=leetcode.cn id=25 lang=python
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        start = ListNode()
        start.next = head
        left = start
        right = start
        for i in range(k):
            if right is not None:
                right = right.next
            else:
                return head
        if right is None:
            return head
        tmp = right.next
        right.next = None
        reverse_list, end = self.reverseList(left.next)
        end.next = self.reverseKGroup(tmp, k)
        start.next = reverse_list
        
        return start.next
        

    def reverseList(self, head):
        res = head
        re_head = ListNode()
        while res:
            tmp = res.next
            res.next = re_head.next
            re_head.next = res
            res = tmp
        return re_head.next, head
        
# @lc code=end

if __name__ == "__main__":
    list_0 = ListNode(5)
    list_1 = ListNode(4, list_0)
    list_2 = ListNode(3, list_1)
    list_3 = ListNode(2, list_2)
    list_4 = ListNode(1, list_3)
    sol = Solution()
    res = sol.reverseKGroup(list_4, 2)
    while res:
        print(res.val)
        res = res.next