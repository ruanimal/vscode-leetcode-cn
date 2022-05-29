#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#
# https://leetcode-cn.com/problems/self-dividing-numbers/description/
#
# algorithms
# Easy (74.75%)
# Likes:    236
# Dislikes: 0
# Total Accepted:    71.3K
# Total Submissions: 90.4K
# Testcase Example:  '1\n22'
#
# 自除数 是指可以被它包含的每一位数整除的数。
#
#
# 例如，128 是一个 自除数 ，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
#
#
# 自除数 不允许包含 0 。
#
# 给定两个整数 left 和 right ，返回一个列表，列表的元素是范围 [left, right] 内所有的 自除数 。
#
#
#
# 示例 1：
#
#
# 输入：left = 1, right = 22
# 输出：[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
#
#
# 示例 2:
#
#
# 输入：left = 47, right = 85
# 输出：[48,55,66,77]
#
#
#
#
# 提示：
#
#
# 1 <= left <= right <= 10^4
#
#
#

from comm import *
# @lc code=start

class Solution:
    cache = set()   # 全局缓存

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [i for i in range(left, right+1) if self.is_valid(i)]

    def is_valid(self, num):
        if num in self.cache:
            return True
        tmp = num
        while tmp > 0:
            if tmp % 10 == 0 or num % (tmp % 10) != 0:
                return False
            tmp = tmp // 10
        self.cache.add(num)
        return True

# @lc code=end

