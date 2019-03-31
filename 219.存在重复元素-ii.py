#
# @lc app=leetcode.cn id=219 lang=python
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
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        index_map = {}
        for i, ele in enumerate(nums):
            index_map.setdefault(ele, []).append(i)
        for key, val in index_map.iteritems():
            if len(val) >= 2:
                val.sort()
                for i in xrange(len(val)-1):
                    if val[i+1] - val[i] <= k:
                        return True
        return False
