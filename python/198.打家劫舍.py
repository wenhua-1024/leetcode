#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#

# @lc code=start
import numpy as np

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return int(self.get_max(nums))
    
    def get_max(self, nums):
        dp = np.zeros((len(nums), 2))
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for idx, num in enumerate(nums):
            if idx == 0:
                continue
            dp[idx][0] = max(dp[idx - 1][0], dp[idx - 1][1])
            dp[idx][1] = dp[idx - 1][0] + num
        return max(dp[len(nums)-1][0], dp[len(nums)-1][1])

# @lc code=end