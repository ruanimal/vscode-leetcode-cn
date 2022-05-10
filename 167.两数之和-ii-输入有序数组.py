#
# @lc app=leetcode.cn id=167 lang=python3
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

from comm import *
# @lc code=start

class SolutionA(object):
    def twoSum(self, numbers: List[int], target: int) -> int:
        """
        hash法, 将number:index存到dict中, 判断 target - number 是否在dict中
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

class Solution(object):
    def twoSum(self, numbers: List[int], target: int) -> int:
        """
        双指针法
        """
        if len(numbers) <= 1:
            return []
        i = 0
        j = len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i+1, j+1]   # 下标从1开始
        return []
# @lc code=end

if __name__ == "__main__":
    s = Solution().twoSum( numbers = [2, 7, 11, 15], target = 9)
    print(s)

