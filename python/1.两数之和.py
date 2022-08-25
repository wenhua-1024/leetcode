#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = {}
        for idx, num in enumerate(nums):
            temp = target - num
            if temp not in res.keys():
                res.update({num: idx})
            else:
                return [res.get(temp), idx]
# @lc code=end
