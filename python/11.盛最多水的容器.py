#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right = len(height)-1
        left = 0
        res = -1
        while(left <= right):
            area = min(height[right], height[left])*(right-left) 
            res = area if res<area else res
            if height[right]< height[left]:
                right -= 1
            else:
                left += 1
        return res
# @lc code=end

