#
# @lc app=leetcode.cn id=307 lang=python3
#
# [307] 区域和检索 - 数组可修改
#
# https://leetcode.cn/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (53.89%)
# Likes:    763
# Dislikes: 0
# Total Accepted:    96.4K
# Total Submissions: 178.9K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# 给你一个数组 nums ，请你完成两类查询。
#
#
# 其中一类查询要求 更新 数组 nums 下标对应的值
# 另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right
#
#
# 实现 NumArray 类：
#
#
# NumArray(int[] nums) 用整数数组 nums 初始化对象
# void update(int index, int val) 将 nums[index] 的值 更新 为 val
# int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含
# ）的nums元素的 和 （即，nums[left] + nums[left + 1], ..., nums[right]）
#
#
#
#
# 示例 1：
#
#
# 输入：
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# 输出：
# [null, 9, null, 8]
#
# 解释：
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1,2,5]
# numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
# 0 <= index < nums.length
# -100 <= val <= 100
# 0 <= left <= right < nums.length
# 调用 update 和 sumRange 方法次数不大于 3 * 10^4 
#
#
#

from comm import *
# @lc code=start
class NumArrayV0:
    """暴力解法, 超时"""

    def __init__(self, nums: List[int]):
        self.nums: List[int] = [0 for _ in nums]
        self.num_sums: List[int] = [0 for _ in nums]
        for idx, i in enumerate(nums):
            self.update(idx, i)

    def update(self, index: int, val: int) -> None:
        gap = (val - self.nums[index])
        self.nums[index] = val
        for i in range(index, len(self.nums)):
            self.num_sums[i] += gap

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.num_sums[right]
        return self.num_sums[right] - self.num_sums[left-1]

'''

'''

class NumArray:
    """Binary Indexed Tree（BIT）
    i & -i 代表取二进制的最低位1, 所代表的数字

    思考这个数字的二进制表示, 没完全懂..
    """

    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums[:]
        self.bit: List[int] = [0] + nums
        for i in range(1, len(self.bit)):
            j = i + (i & -i)
            if j < len(self.bit):
                self.bit[j] += self.bit[i]

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        index += 1
        while index <= len(self.bit)-1:
            self.bit[index] += delta
            index += index & (-index)

    def query(self, index: int) -> int:
        total = 0
        index += 1
        while index > 0:
            total += self.bit[index]
            index -= index & -index
        return total

    def sumRange(self, left: int, right: int) -> int:
        return self.query(right) - self.query(left-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end

if __name__ == '__main__':
    numArray = NumArray([1, 3, 5, 7, 11, 13])
    print(numArray.nums, numArray.bit)
    print(numArray.sumRange(0,2))
    print(numArray.sumRange(1,2))
    numArray.update(1, 2)
    print(numArray.nums, numArray.bit)
    print(numArray.sumRange(0, 2))
