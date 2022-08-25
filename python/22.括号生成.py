#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        res = []
        tmp = []
        for i in range(n*2):
            if len(res) == 0:
                res.append("(")
                continue
            for s in res:
                if s.count('(') > s.count(')'):
                    if s.count('(') < n:
                        tmp.append(s + '(')
                        tmp.append(s + ')')
                    elif s.count('(') == n:
                        tmp.append(s + ')')
                elif s.count('(') == s.count(')'):
                    if s.count('(') < n:
                        tmp.append(s + '(')
            res = tmp
            tmp = []
        return res

# @lc code=end

