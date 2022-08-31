#
# @lc app=leetcode.cn id=34 lang=python
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mid = self.search(nums, target, 0, len(nums)-1)
        if mid == -1:
            return [-1, -1]
        left = mid
        right = mid
        while nums[left] == target:
            left -= 1
            if left < 0:
                break
        while nums[right] == target:
            right += 1
            if right > len(nums)-1:
                break
            
        return [left + 1, right-1]
    def search(self, nums, target, start, end):
        if start > end:
            return -1
        mid = int((start + end)) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.search(nums, target, start, mid - 1)
        else:
            return self.search(nums, target, mid + 1, end)
# @lc code=end

