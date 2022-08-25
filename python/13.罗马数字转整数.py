#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roma = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        ind = 0
        while(ind<len(s)):
            if ind == len(s)-1:
                res += roma[s[ind]]
            else:
                if roma[s[ind]] < roma[s[ind+1]]:
                    res += roma[s[ind+1]] - roma[s[ind]]
                    ind += 1
                else:
                    res += roma[s[ind]]
            ind += 1
        return res

# @lc code=end

