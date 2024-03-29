#
# @lc app=leetcode.cn id=1013 lang=python3
#
# [1013] 将数组分成和相等的三个部分
#
# https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum/description/
#
# algorithms
# Easy (43.28%)
# Likes:    9
# Dislikes: 0
# Total Accepted:    1.9K
# Total Submissions: 4.3K
# Testcase Example:  '[0,2,1,-6,6,-7,9,1,2,0,1]'
#
# 给定一个整数数组 A，只有我们可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
#
# 形式上，如果我们可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ...
# + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。
#
#
#
# 示例 1：
#
# 输出：[0,2,1,-6,6,-7,9,1,2,0,1]
# 输出：true
# 解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
#
#
# 示例 2：
#
# 输入：[0,2,1,-6,6,7,9,-1,2,0,1]
# 输出：false
#
#
# 示例 3：
#
# 输入：[3,3,6,5,-2,2,5,1,-9,4]
# 输出：true
# 解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
#
#
#
#
# 提示：
#
#
# 3 <= A.length <= 50000
# -10000 <= A[i] <= 10000
#
#
#
class Solution(object):
    def canThreePartsEqualSum(self, A):
        """求和
        依次累加, 判断是否等于 sum_a // 3

        边界case处理比较麻烦, 直接抄官方题解
        """
        s = sum(A)
        if s % 3 != 0:
            return False
        target = s // 3
        n, i, cur = len(A), 0, 0
        while i < n:
            cur += A[i]
            if cur == target:
                break
            i += 1
        if cur != target:
            return False
        j = i + 1
        while j + 1 < n:  # 需要满足最后一个数组非空
            cur += A[j]
            if cur == target * 2:
                return True
            j += 1
        return False

if __name__ == "__main__":
    s = Solution().canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1])
    print(s)

