#
# @lc app=leetcode.cn id=322 lang=python
#
# [322] 零钱兑换
#

# @lc code=start
class Solution(object):
    dp = {}
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = {}
        self.get_min_coins(coins, amount, dp)
        return dp[amount]
        
    def get_min_coins(self, coins, amount, dp):
        if amount in dp:
            return dp[amount]
        if amount == 0:
            dp[amount] = 0
            return dp[amount]
        min_coins = []
        for coin in coins:
            if amount-coin == 0:
                min_coins.append(1)
                break
            elif amount-coin > 0:
                self.get_min_coins(coins, amount-coin, dp)
                if dp[amount-coin] > 0:
                    min_coins.append(dp[amount-coin] + 1)
        dp[amount] = min(min_coins) if len(min_coins) > 0 else -1

        return 

# if __name__ == "__main__":
#     coins = [1,2,5]
#     amount = 11
#     so = Solution()
#     res = so.coinChange(coins, amount)
#     print(res)
# @lc code=end

