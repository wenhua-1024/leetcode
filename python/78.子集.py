#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
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

