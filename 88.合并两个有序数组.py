#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (42.48%)
# Total Accepted:    36.2K
# Total Submissions: 83.3K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
#
# 说明:
#
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#
#
# 示例:
#
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出: [1,2,2,3,5,6]
#
#


class SolutionA(object):
    def merge(self, nums1: list, m: int, nums2: list, n: int):
        """
        暴力法
        思路： 将nums2中的逐个插入到nums1合适的位置，调整m的大小，如果某一个nums2中的值大于nums1最后一个值
              则将nums2剩下的值全部添加到nums1后边
        """

        for i in range(n):
            for j in range(m):
                if nums2[i] < nums1[j]:
                    nums1.insert(j, nums2[i])
                    nums1.pop()
                    m += 1
                    break
                if m == len(nums1):
                    return
            else:
                for k, num in enumerate(nums2[i:]):
                    nums1[m+k] = num
                return

class Solution(object):
    def merge(self, nums1: list, m: int, nums2: list, n: int):
        """
        反方向开始合并操作, 避免insert
        """

        i = m-1
        j = n-1
        while i+j+1 >= 0:
            # print(i, j, nums1)
            if i >= 0 and j >= 0:
                if nums1[i] >= nums2[j]:
                    nums1[i+j+1] = nums1[i]
                    i -= 1
                else:
                    nums1[i+j+1] = nums2[j]
                    j -= 1
            elif j < 0:
                nums1[i+j+1] = nums1[i]
                i -= 1
            else:  # i < 0
                nums1[i+j+1] = nums2[j]
                j -= 1
        return nums1

# @lc code=end

s = Solution().merge(
    nums1 = [1,2,3,0,0,0], m = 3,
    nums2 = [2,5,6],       n = 3,
)
print(s)

