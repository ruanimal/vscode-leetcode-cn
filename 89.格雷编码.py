#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#
# https://leetcode-cn.com/problems/gray-code/description/
#
# algorithms
# Medium (64.25%)
# Likes:    68
# Dislikes: 0
# Total Accepted:    7.7K
# Total Submissions: 11.9K
# Testcase Example:  '2'
#
# 格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
#
# 给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。
#
# 示例 1:
#
# 输入: 2
# 输出: [0,1,3,2]
# 解释:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
#
# 对于给定的 n，其格雷编码序列并不唯一。
# 例如，[0,2,3,1] 也是一个有效的格雷编码序列。
#
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
#
# 示例 2:
#
# 输入: 0
# 输出: [0]
# 解释: 我们定义格雷编码序列必须以 0 开头。
# 给定编码总位数为 n 的格雷编码序列，其长度为 2^n。当 n = 0 时，长度为 2^0 = 1。
# 因此，当 n = 0 时，其格雷编码序列为 [0]。
#
#
#
class SolutionA(object):
    def grayCode(self, n: int) -> list:
        """
        位运算, 从前面加, 已有的数能利用上, 比较绕
        """
        if n == 0:
            return [0]
        ans = [0, 1]
        for i in range(2, n+1):
            tmp = 2 ** (i-1)
            ans = ans + [(x | tmp) for x in ans[::-1]]
        print(['{:0>32}'.format(bin(i)[2:])[-n:] for i in ans])
        return ans

class Solution(object):
    def grayCode(self, n: int) -> list:
        """
        位运算, 直接生成(从后面加), 但是较慢
        """
        ans = [0]
        for i in range(n):
            new_ans = []
            for idx, i in enumerate(ans):
                # 往末尾追加的时候0, 1得交替放
                if idx % 2 == 0:
                    new_ans.append(i << 1 )
                    new_ans.append((i << 1) | 1)
                else:
                    new_ans.append((i << 1) | 1)
                    new_ans.append(i << 1 )
            ans = new_ans
        return ans

if __name__ == "__main__":
    s = Solution().grayCode(2)
    print(s)
    s = SolutionA().grayCode(3)
    print(s)
    s = Solution().grayCode(3)
    print(s)

