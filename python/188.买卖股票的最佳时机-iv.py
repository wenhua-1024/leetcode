#
# @lc app=leetcode.cn id=188 lang=python
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
import numpy as np
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        days = len(prices)
        if days <= 0:
            return 0
        # dp_table = [[[0]*2]*(k+1)]*days
        dp_table = np.zeros((days, k+1, 2))
        for n_ in range(days):
            dp_table[n_][0][0] = 0
            dp_table[n_][0][1] = -2000

        for n_ in range(days):
            for k_ in range(k, 0, -1):
                if n_-1 == -1:
                    dp_table[n_][k_][0] = 0
                    dp_table[n_][k_][1] = -prices[n_]
                    continue
                dp_table[n_][k_][0] = \
                    max(dp_table[n_-1][k_][0], dp_table[n_-1][k_][1] + prices[n_])
                dp_table[n_][k_][1] = \
                    max(dp_table[n_-1][k_][1], dp_table[n_-1][k_-1][0] - prices[n_])
        return int(dp_table[days-1][k][0])
# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    res = sol.maxProfit(2, [3,3,5,0,0,3,1,4])
    print(res)
    for i in range(10, 0, -1):
        print(i)

