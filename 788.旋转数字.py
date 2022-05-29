#
# @lc app=leetcode.cn id=788 lang=python3
#
# [788] 旋转数字
#
# https://leetcode-cn.com/problems/rotated-digits/description/
#
# algorithms
# Medium (61.08%)
# Likes:    108
# Dislikes: 0
# Total Accepted:    20K
# Total Submissions: 32.6K
# Testcase Example:  '10'
#
# 我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。要求每位数字都要被旋转。
#
# 如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；2 和 5
# 可以互相旋转成对方（在这种情况下，它们以不同的方向旋转，换句话说，2 和 5 互为镜像）；6 和 9
# 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。
#
# 现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？
#
#
#
# 示例：
#
# 输入: 10
# 输出: 4
# 解释:
# 在[1, 10]中有四个好数： 2, 5, 6, 9。
# 注意 1 和 10 不是好数, 因为他们在旋转之后不变。
#
#
#
#
# 提示：
#
#
# N 的取值范围是 [1, 10000]。
#
#
#

# @lc code=start
class Solution:
    """暴力法加缓存"""

    trans_map = {'1':'1', '0':'0', '8':'8', '2': '5', '5': '2', '6': '9', '9': '6'}
    cache = set()

    def rotatedDigits(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            if self.is_valid(i):
                count += 1
        return count

    def is_valid(self, num):
        if num in self.cache:
            return True
        str_num = list(str(num))
        tmp = []
        for j in str_num:
            if j in self.trans_map:
                tmp.append(self.trans_map[j])
            else:
                break
        if len(tmp) == len(str_num) and tmp != str_num:
            self.cache.add(num)
            return True
        return False

# TODO(rlj): 动态规划.
# @lc code=end

