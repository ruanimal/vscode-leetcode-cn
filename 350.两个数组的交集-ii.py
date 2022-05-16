#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#
# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (38.62%)
# Total Accepted:    28.9K
# Total Submissions: 71.8K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# 给定两个数组，编写一个函数来计算它们的交集。
#
# 示例 1:
#
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]
#
#
# 示例 2:
#
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]
#
# 说明：
#
#
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
# 我们可以不考虑输出结果的顺序。
#
#
# 进阶:
#
#
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
#
#
#
class SolutionA:
    def intersect(self, nums1: list, nums2: list) -> list:
        """使用第349题的暴力法
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
                    begin_j = j+1
                    break
                else:
                    j += 1
        return ret

from collections import Counter

class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        """哈希计数法
        """

        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        res = []
        for num, cnt in (cnt1 & cnt2).items():
            res.extend([num] * cnt)
        return res

if __name__ == "__main__":
    t = Solution().intersect(nums1 = [4,4,4,9,5,8], nums2 = [9,4,9,8,4])
    print(t)


