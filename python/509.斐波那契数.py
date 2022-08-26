#
# @lc app=leetcode.cn id=509 lang=python
#
# [509] 斐波那契数
#

# @lc code=start

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0
        if n == 1:
            return 1
        table = [0, 1]
        count = 2
        while count <= n:
            table.append(sum(table[-2:]))
            count += 1
        return table[-1]
# @lc code=end

