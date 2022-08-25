#
# @lc app=leetcode.cn id=18 lang=python
#
# [18] 四数之和
#

# @lc code=start
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        res = []
        nums.sort()
        
        for ll in range(len(nums) - 2):
            for rr in range(2, len(nums)):
                if ll == rr:
                    continue
                left = ll+1
                right = rr - 1
                while left < right:
                    n_sum = nums[ll] + nums[left]  + nums[right] + nums[rr]
                    if n_sum == target:
                        if [nums[ll], nums[left], nums[right], nums[rr]] not in res:
                            res.append([nums[ll], nums[left], nums[right], nums[rr]])
                        left += 1
                        right -= 1
                    elif n_sum < target:
                        left += 1
                    else:
                        right -= 1
        return res
# @lc code=end

if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    sol = Solution()
    res = sol.fourSum(nums, target)
    print(res)

