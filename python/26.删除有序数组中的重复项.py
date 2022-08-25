#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ind = 1
        while ind < len(nums):
            if nums[ind] == nums[ind-1]:
                nums.pop(ind)
            else:
                ind += 1

        return len(nums)
# @lc code=end

