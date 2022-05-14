#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
# https://leetcode-cn.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (32.81%)
# Total Accepted:    10.9K
# Total Submissions: 32.1K
# Testcase Example:  '[1,2,3,1]\n3'
#
# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j
# 的差的绝对值最大为 k。
#
# 示例 1:
#
# 输入: nums = [1,2,3,1], k = 3
# 输出: true
#
# 示例 2:
#
# 输入: nums = [1,0,1,1], k = 1
# 输出: true
#
# 示例 3:
#
# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false
#
#
class Solution(object):
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        """
        计数法
        """
        index_map = {}
        for i, ele in enumerate(nums):
            if ele not in index_map:
                index_map[ele] = [i]
            else:
                index_map[ele].append(i)
                if index_map[ele][-1] - index_map[ele][-2] <= k:
                    return True
        return False

# TODO(rlj): 可以用双指针法.
