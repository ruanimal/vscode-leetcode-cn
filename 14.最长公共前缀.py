#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (33.02%)
# Likes:    582
# Dislikes: 0
# Total Accepted:    87.6K
# Total Submissions: 260.1K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#

class Tried(dict):
    def __init__(self):
        self.count = 0


class Solution_A(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        前缀树解法
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        tried = Tried()
        for s in strs:
            tmp = tried
            for i in s:
                if i not in tmp:
                    tmp[i] = Tried()
                tmp.count += 1
                tmp = tmp[i]

        ans = ''
        tmp = tried
        while tried:
            if tried.count != len(strs) or len(tried) > 1:
                break
            k, tried = list(tried.items())[0]
            ans += k
        return ans


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        直接取所有字符串的第n位求交集
            如果集合大小为1, 则前缀包含改字符
            否则跳出
        """

        res = []
        for i in range(min(len(i) for i in strs)):
            if len(set(s[i] for s in strs)) == 1:
                res.append(strs[0][i])
            else:
                break
        return ''.join(res)


if __name__ == "__main__":
    s = Solution().longestCommonPrefix(["flower","flow","flight"])
    print(s)
    s = Solution().longestCommonPrefix(["a","b","c"])
    print(s)
    s = Solution().longestCommonPrefix(["baaa","b"])
    print(s)
    s = Solution().longestCommonPrefix(["b","b"])
    print(s)
    s = Solution().longestCommonPrefix(["b","bcb"])
    print(s)
    s = Solution().longestCommonPrefix(["b",""])
    print(s)


