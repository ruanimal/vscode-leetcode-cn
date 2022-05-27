#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#
# https://leetcode-cn.com/problems/longest-harmonious-subsequence/description/
#
# algorithms
# Easy (40.17%)
# Likes:    46
# Dislikes: 0
# Total Accepted:    3.3K
# Total Submissions: 8K
# Testcase Example:  '[1,3,2,2,5,2,3,7]'
#
# 和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
#
# 现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。
#
# 示例 1:
#
#
# 输入: [1,3,2,2,5,2,3,7]
# 输出: 5
# 原因: 最长的和谐数组是：[3,2,2,2,3].
#
#
# 说明: 输入的数组长度最大不超过20,000.
#
#

from comm import *
# @lc code=start

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """计数排序法

        如果排序后相邻的数字之差为1, 则长度就是这两个数字个数之和
        """
        from collections import Counter

        if not nums:
            return 0
        counter = Counter(nums)
        counter_list = sorted(counter.items(), key=lambda i: i[0])
        max_val = 0
        for i in range(1, len(counter_list)):
            a, b = counter_list[i-1], counter_list[i]
            if (b[0]-a[0]) != 1:
                continue
            max_val = max(max_val, a[1] + b[1])
        return max_val

# @lc code=end


if __name__ == "__main__":
    s = Solution().findLHS([1,3,2,2,5,2,3,7])
    print(s)
    s = Solution().findLHS([1,1,1,1])
    print(s)
    s = Solution().findLHS([1,3,5,7,9,11,13,15,17])
    print(s)

