#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        res = head
        while list1 or list2:
            tmp = ListNode()
            if list1 and list2:
                if list1.val <= list2.val:
                    tmp.val = list1.val
                    list1 = list1.next
                else:
                    tmp.val = list2.val
                    list2 = list2.next
            elif list1:
                tmp.val = list1.val
                list1 = list1.next
            else:
                tmp.val = list2.val
                list2 = list2.next
            res.next = tmp
            res = res.next

        return head.next
# @lc code=end

# if __name__ == "__main__":
#     list1 = ListNode(4)
#     list2 = ListNode(2)
#     sol = Solution()
#     res = sol.mergeTwoLists(list1, list2)
#     print(res)

