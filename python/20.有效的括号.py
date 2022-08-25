#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = []
        for c in s:
            if c in ['{', '[', '(']:
                tmp.append(c)
            elif len(tmp) == 0:
                return False
            else:
                if c == '}' and tmp.pop() == '{':
                    continue
                elif c == ']' and tmp.pop() == '[':
                    continue
                elif c == ')' and tmp.pop() == '(':
                    continue
                else:
                    return False
        if len(tmp) > 0:
            return False
        return True
# @lc code=end

