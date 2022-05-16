#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#
# https://leetcode-cn.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (59.39%)
# Total Accepted:    16.8K
# Total Submissions: 27.4K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# 给定两个数组，编写一个函数来计算它们的交集。
#
# 示例 1:
#
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2]
#
#
# 示例 2:
#
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [9,4]
#
# 说明:
#
#
# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。
#
#
#
class SolutionA:
    def intersection(self, nums1: list, nums2: list) -> list:
        """
        暴力法
        排序, 然后逐个比较大小, 用列表储存相同元素, 比较时记住上一轮结束比较的位置
        """
        if not nums1 or not nums2:
            return

        nums1.sort()
        nums2.sort()

        ret = []
        begin_j = 0
        for i in range(len(nums1)):
            j = begin_j
            while j < len(nums2):
                if nums1[i] < nums2[j]:
                    break
                elif nums1[i] == nums2[j]:
                    ret.append(nums1[i])
                    begin_j = j
                    break
                else:
                    j += 1
        return list(set(ret))


class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
        """集合法"""

        return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    t = Solution().intersection(nums1 = [4,9,5,8], nums2 = [9,4,9,8,4])
    print(t)
