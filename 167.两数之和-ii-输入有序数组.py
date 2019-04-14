#
# @lc app=leetcode.cn id=167 lang=python
#
# [167] 两数之和 II - 输入有序数组
#
# https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Easy (46.75%)
# Total Accepted:    21.2K
# Total Submissions: 44.2K
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
#
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
#
# 说明:
#
#
# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
#
#
# 示例:
#
# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
#
#
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_map = {}
        for idx, elem in enumerate(numbers):
            index_map.setdefault(elem, []).append(idx)

        for idx, i in enumerate(numbers):
            extra = (target - i)
            extra_idx = index_map.get(extra, [])
            for idx2 in extra_idx:
                if idx == idx2:
                    continue
                return [idx+1, idx2+1]
        return []

if __name__ == "__main__":
    s = Solution().twoSum( numbers = [2, 7, 11, 15], target = 9)
    print(s)

