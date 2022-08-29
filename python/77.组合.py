#
# @lc app=leetcode.cn id=77 lang=python
#
# [77] 组合
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        tmp = []
        self.trace_back(1, n, k, tmp, res)
        return sorted(res)

    def trace_back(self, start, n, k, tmp, res):
        if len(tmp) == k:
            res.append(tmp[:])
            return
        for start in range(start, n+1):
            tmp.append(start)
            self.trace_back(start + 1, n, k, tmp, res)
            tmp.pop()

            
            
# @lc code=end

