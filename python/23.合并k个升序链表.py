#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # fil_lists = []
        # for list_ in lists:
        #     if list_ is None:
        #         continue
        #     fil_lists.append(list_)
        
        heap = []
        head = ListNode()
        res = head
        for list_ in lists:
            if list_ is not None:
                heapq.heappush(heap, (list_.val, list_))
        while len(heap) > 0:
            # lists = filter(self.filter_none, lists)
            tmp = ListNode()
            (min_, list_) = heapq.heappop(heap)
            tmp.val = min_
            if list_.next is not None:
                list_ = list_.next
                heapq.heappush(heap, (list_.val, list_))
            res.next = tmp
            res = res.next
        return head.next 
# @lc code=end
        