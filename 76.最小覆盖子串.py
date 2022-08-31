#
# @lc app=leetcode.cn id=76 lang=python
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = {}
        windows = {}
        valid = 0
        for key in t:
            if key in need:
                need[key] += 1
            else:
                need[key] = 1
        left = 0
        right = 0
        min_len = 1000000
        start = 0
        while right < len(s):
            c = s[right]
            if c in need:
                if c in windows:
                    windows[c] += 1
                else:
                    windows[c] = 1
                if windows[c] == need[c]:
                    valid += 1
            right += 1
            while valid == len(need):
                if right - left < min_len:
                    start = left
                    min_len = right - left
                c = s[left]
                if c in need:
                    windows[c] -= 1
                    if windows[c] < need[c]: 
                        valid -= 1
                left += 1
        return s[start: start + min_len] if min_len < 1000000 else ""

        
# @lc code=end

