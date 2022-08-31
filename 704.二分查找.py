#
# @lc app=leetcode.cn id=704 lang=python
#
# [704] 二分查找
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search(nums, target, 0, len(nums)-1)
    def binary_search(self, nums, target, start, end):
        if start > end:
            return -1
        mid = int((start + end) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary_search(nums, target, start, mid-1)
        else:
            return self.binary_search(nums, target, mid+1, end)
# @lc code=end

