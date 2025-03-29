#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (33.41%)
# Total Accepted:    35.3K
# Total Submissions: 105.6K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
#
#
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5
#
#
#


class SolutionA:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        进行一次归并, 然后求中位数
        """
        result = []
        l = r = 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                result.append(nums1[l])
                l += 1
            else:
                result.append(nums2[r])
                r += 1
        result += nums1[l:]
        result += nums2[r:]
        if len(result) % 2 == 1:
            return result[len(result)//2]
        else:
            return (result[len(result)//2-1]+result[len(result)//2])/2.0

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]):
        pass

