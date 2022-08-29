#
# @lc app=leetcode.cn id=51 lang=python
#
# [51] N 皇后
#

# @lc code=start
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        dp = [True] * n
        c = []
        for i in range(n):
            tmp = ""
            for j in range(n):
                if i == j:
                    tmp += "Q"
                else:
                    tmp += "."
            c.append(tmp)

        return self.get_n_queens(c, n)
    def get_n_queens(self, nums, n):

        res = []
        if len(nums) == 1:
            res.append(nums)
            return res
        if len(nums) == 0:
            res.append([])
            return res
        for ind, num in enumerate(nums):
            nums.pop(ind)
            inp = nums[:]
            nums.insert(ind, num)
            ress = self.get_n_queens(inp, n)
            for tmp in ress:
                if self.judge(num, tmp, n, flag="left") and self.judge(num, tmp, n, flag="right"):
                    tmp.append(num)
                    res.append(tmp)
        return res
    def judge(self, s, strs, n, flag="left"):
        length = len(strs)
        ind = s.find('Q')
        for index, st in enumerate(strs):
            if flag == "left" and ind+index-length >= 0 and ind+index-length < n:
                if st[ind+index-length] == 'Q':
                    return False
            elif flag == "right" and ind+length-index >= 0 and ind+length-index < n:
                if st[ind+length-index] == 'Q':
                    return False
        return True
                    
# @lc code=end

