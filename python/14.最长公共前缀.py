#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: 
            return ""
        s1 = min(strs)
        s2 = max(strs)
        for i,x in enumerate(s1):
            if x!= s2[i]:
                return s2[:i]
        return s1


# @lc code=end

