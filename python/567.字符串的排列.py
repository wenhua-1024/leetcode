#
# @lc app=leetcode.cn id=567 lang=python
#
# [567] 字符串的排列
#

# @lc code=start
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_num = {}
        count = 0
        for s in s1:
            if s not in s1_num:
                s1_num.update({s: 1})
            else:
                self.update_dict_value(s1_num, s, s1_num[s]+1)
            count += 1
        s_num_ = s1_num.copy()
        count_ori = count
        start = 0
        end = 0
        while count != 0 and end < len(s2):
            if s2[end] not in s1_num:
                s1_num = s_num_.copy()
                count = count_ori
                end += 1
                start = end
                continue
            elif s1_num[s2[end]] <= 0:
                count = self.rollback(s2, s1_num, count, start, start)
                start += 1
            else:
                self.update_dict_value(s1_num, s2[end], s1_num[s2[end]]-1)
                end += 1
                count -= 1
            if (end - start) == len(s1):
                if count == 0:
                    return True
                else:
                    count = self.rollback(s2, s1_num, count, start, start)
                    start += 1
            if end >= len(s2):
                return False
        return False
    def rollback(self, s2, s1_num, count, start, end):
        while start <= end:
            self.update_dict_value(s1_num, s2[start], s1_num[s2[start]] + 1)
            count += 1
            start += 1
        return count
    def update_dict_value(self, s1_num, key, target):
        s1_num.update({key: target})


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    res = sol.checkInclusion("adc", "dcba")
    print(res)

