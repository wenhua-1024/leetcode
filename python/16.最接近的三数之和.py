#
# @lc app=leetcode.cn id=16 lang=python
#
# [16] 最接近的三数之和
#

# @lc code=start
import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sys.maxint
        ind = 0
        while ind < len(nums):
            c = nums[ind]
            left = ind + 1
            right = len(nums)-1
            while(left<right):
                _sum = nums[left] + nums[right] + c
                if abs(_sum - target) < abs(res - target):
                    res = _sum
                if _sum == target:
                    return target
                if _sum> target:
                    right -= 1
                else:
                    left += 1
            ind += 1
        return res
# @lc code=end

