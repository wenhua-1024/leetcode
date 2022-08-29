#
# @lc app=leetcode.cn id=47 lang=python
#
# [47] 全排列 II
#

# @lc code=start
class Solution(object):
    res = []
    tmp = []
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        nums = sorted(nums)
        self.res = []
        self.tmp = []
        flag = [True] * len(nums)
        self.track_back(nums, flag)
        return self.res
    def track_back(self, nums, flag):
        if sum(flag) == 0:
            if self.tmp[:] not in self.res:
                self.res.append(self.tmp[:])
            return
        for ind, _ in enumerate(flag):
            if not flag[ind]:
                continue
            flag[ind] = False
            self.tmp.append(nums[ind])
            self.track_back(nums, flag)
            self.tmp.pop()
            flag[ind] = True
# @lc code=end

