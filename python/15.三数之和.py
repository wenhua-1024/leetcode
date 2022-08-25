#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: 
            return []
        nums.sort()
        res = []
        ind = 0
        # c = nums[0]
        while ind < len(nums):
            # if c != nums[ind]:
            #     c = nums[ind]
            # else:
            #     ind += 1
            #     continue
            c = nums[ind]
            left = ind + 1
            right = len(nums)-1
            while(left<right):
                if nums[left] + nums[right] + c == 0:
                    if [c, nums[left], nums[right]] not in res:
                        res.append([c, nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] + c > 0:
                    right -= 1
                else:
                    left += 1
            ind += 1
        return res

# @lc code=end

