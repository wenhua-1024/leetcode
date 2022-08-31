#
# @lc app=leetcode.cn id=752 lang=python
#
# [752] 打开转盘锁
#

# @lc code=start
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if target in deadends:
            return -1
        if "0000" in deadends:
            return -1
        return self.bfs(deadends, target)
    def bfs(self, deadends, target):
        deadends = set(deadends)
        table = set()
        depth = 0
        path = []
        path.append("0000")
        table.add("0000")
        while len(path) > 0:
            length = len(path)
            depth += 1
            for ind in range(length):
                node = path.pop(0)
                if node == target:
                    return depth-1
                next_nodes = self.generate(node, deadends, table)
                for nnode in next_nodes:
                    if nnode == target:
                        return depth
                    table.add(nnode)
                    path.append(nnode)
        return -1
                    
    def generate(self, start, deadends, table):
        res = []
        for ind, c in enumerate(start):
            tmp = start[:ind] + self.get_next(c) + start[ind+1:]
            if tmp not in deadends and tmp not in table:
                res.append(tmp[:])
            tmp = start[:ind] + self.get_pre(c) + start[ind+1:]
            if tmp not in deadends and tmp not in table:
                res.append(tmp[:])
        return res
    def get_next(self, c):
        if c == '9':
            return '0'
        return str(int(c) + 1)
    def get_pre(self, c):
        if c == '0':
            return '9'
        return str(int(c) - 1)
# @lc code=end
