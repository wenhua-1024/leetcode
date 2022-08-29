#
# @lc app=leetcode.cn id=90 lang=python
#
# [90] 子集 II
#

# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return [[]]
        res = []
        tmp = []
        self.trace_back(nums, res, tmp)
        res.append([])
        return sorted(res)

    def trace_back(self, nums, res, tmp):
        if len(nums) == 0:
            return
        for ind, _ in enumerate(nums):
            po = nums.pop(ind)
            tmp.append(po)
            ite = sorted(tmp[:])
            if ite not in res :
                res.append(ite)
                self.trace_back(nums, res, tmp)
            tmp.pop()
            nums.insert(ind, po)
# @lc code=end

