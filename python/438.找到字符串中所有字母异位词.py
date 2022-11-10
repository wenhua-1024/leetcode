#
# @lc app=leetcode.cn id=438 lang=python
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        s1_num = {}
        count = 0
        for s_ in p:
            if s_ not in s1_num:
                s1_num.update({s_: 1})
            else:
                self.update_dict_value(s1_num, s_, s1_num[s_]+1)
            count += 1
        s_num_ = s1_num.copy()
        count_ori = count
        start = 0
        end = 0
        res = []
        while count != 0 and end < len(s):
            if s[end] not in s1_num:
                s1_num = s_num_.copy()
                count = count_ori
                end += 1
                start = end
                continue
            elif s1_num[s[end]] <= 0:
                count = self.rollback(s, s1_num, count, start, start)
                start += 1
            else:
                self.update_dict_value(s1_num, s[end], s1_num[s[end]]-1)
                end += 1
                count -= 1
            if (end - start) == len(p):
                if count == 0:
                    res.append(start)
                    count = self.rollback(s, s1_num, count, start, start)
                    start += 1
                else:
                    count = self.rollback(s, s1_num, count, start, start)
                    start += 1
            if end >= len(s):
                break
        return res
    def rollback(self, s2, s1_num, count, start, end):
        while start <= end:
            self.update_dict_value(s1_num, s2[start], s1_num[s2[start]] + 1)
            count += 1
            start += 1
        return count
    def update_dict_value(self, s1_num, key, target):
        s1_num.update({key: target})
# @lc code=end

