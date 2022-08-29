#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#

# @lc code=start
class Solution(object):
    res = []
    tmp = []
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        self.res = []
        self.tmp = []
        flag = [True] * len(nums)
        self.track_back(nums, flag)
        return self.res
    def track_back(self, nums, flag):
        if sum(flag) == 0:
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

