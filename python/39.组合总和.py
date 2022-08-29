#
# @lc app=leetcode.cn id=39 lang=python
#
# [39] 组合总和
#

# @lc code=start
class Solution(object):
    res = []
    tmp = []
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        self.res = []
        self.tmp = []
        self.track_back(0, candidates, target)
        return self.res

    def track_back(self, start, candidates, target):
        if sum(self.tmp) > target:
            return
        elif sum(self.tmp) == target:
            self.res.append(self.tmp[:])
            return
        for ind in range(start, len(candidates)):
            self.tmp.append(candidates[ind])
            self.track_back(ind, candidates, target)
            self.tmp.pop()

# @lc code=end

