#
# @lc app=leetcode.cn id=40 lang=python
#
# [40] 组合总和 II
#

# @lc code=start
class Solution(object):
    res = []
    tmp = []
    table = []
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if sum(candidates) < target:
            return []
        new_candidates = list(filter(lambda x: x <= target, candidates))
        candidates = sorted(new_candidates)
        self.res = []
        self.tmp = []
        self.table = []
        self.track_back(0, candidates, target)
        return self.res

    def track_back(self, start, candidates, target):
        
        if sum(self.tmp) > target:
            self.table.append(self.tmp[:])
            return
        elif sum(self.tmp) == target:
            if self.tmp not in self.res:
                self.res.append(self.tmp[:])
            if self.tmp not in self.table:
                self.table.append(self.tmp[:])
            return
        for ind in range(start, len(candidates)):
            if ind > start and candidates[ind] == candidates[ind-1]:
                continue
            self.tmp.append(candidates[ind])
            
            if self.tmp not in self.table:
                self.track_back(ind+1, candidates, target)
            self.tmp.pop()
# @lc code=end

