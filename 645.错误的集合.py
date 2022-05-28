#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#
# https://leetcode-cn.com/problems/set-mismatch/description/
#
# algorithms
# Easy (35.54%)
# Likes:    46
# Dislikes: 0
# Total Accepted:    4.2K
# Total Submissions: 11.4K
# Testcase Example:  '[1,2,2,4]'
#
# 集合 S 包含从1到 n
# 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。
#
# 给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
#
# 示例 1:
#
#
# 输入: nums = [1,2,2,4]
# 输出: [2,3]
#
#
# 注意:
#
#
# 给定数组的长度范围是 [2, 10000]。
# 给定的数组是无序的。
#
#
#

from comm import *
# @lc code=start

class SolutionA:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """dict计数法
        """

        n = len(nums)
        dup = lose = None
        tmp = {}
        for i in nums:
            tmp[i] = tmp.get(i, 0) + 1
            if tmp[i] > 1:
                dup = i
                break
        lose = n*(n+1)//2 + dup - sum(nums)
        return [dup, lose]

class SolutionB:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """原地排序法
        """

        i = 0
        dup = lose = None
        while i < len(nums):
            if nums[nums[i]-1] != nums[i]:  # 使 nums[i] 上的数字回到正确的位置上
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:  # nums[i] 已经在正确的位置上, 或者 nums[i] 就是重复元素
                if nums[i] != i + 1:   # nums[i] 的位置不对, 就是重复元素
                    dup = nums[i]
                    lose = i + 1   # 最后重复元素所在位置就是缺少的元素
                i += 1
        return [dup, lose]

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """数学法
        sum(nums) - dup + lose = (1 + length) * length / 2
        dup = sum(nums) - sum(set(nums))
        lose = (1 + length) * length / 2 - sum(nums) + dup
        """

        sum_nums = sum(nums)
        dup = sum_nums - sum(set(nums))
        lose = (1 + len(nums)) * len(nums) // 2 - sum_nums + dup
        return [dup, lose]
 # @lc code=end

if __name__ == "__main__":
    s = Solution().findErrorNums(nums = [8,7,3,5,3,6,1,4])
    print(s)
    s = Solution().findErrorNums(nums = [1, 2, 2, 3, 5, 6, 7, 8, 9, 4])
    print(s)

