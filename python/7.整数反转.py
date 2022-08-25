#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x>0 else -1
        x = flag * x
        res = str(x)[::-1]
        y = long(res)

        return flag*y if y<pow(2, 31) else 0


# @lc code=end

