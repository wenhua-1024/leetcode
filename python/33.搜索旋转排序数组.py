#
# @lc app=leetcode.cn id=33 lang=python
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        ind = -1
        while left <= right:
            mid = int((left + right - 1)/2 + 1)
            if nums[mid] < nums[mid-1]:
                ind = mid
            if nums[mid]> nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        if ind < 0:
            return self.search_(nums, target, 0, len(nums)-1)
        elif target < nums[0]:
            return self.search_(nums, target, ind, len(nums)-1)
        elif target > nums[0]:
            return self.search_(nums, target, 0, ind-1)
        return 0
    
    def search_(self, nums, target, begin, end):
        left = begin
        right = end
        while left <= right:
            mid = int((left + right - 1)/2 + 1)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1
# @lc code=end

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    sol = Solution()
    res = sol.search(nums, target)
    print(res)
