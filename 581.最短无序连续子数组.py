#
# @lc app=leetcode.cn id=581 lang=python
#
# [581] 最短无序连续子数组
#
# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Easy (31.75%)
# Likes:    118
# Dislikes: 0
# Total Accepted:    5.2K
# Total Submissions: 15.8K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
#
# 你找到的子数组应是最短的，请输出它的长度。
#
# 示例 1:
#
#
# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
#
#
# 说明 :
#
#
# 输入的数组长度范围在 [1, 10,000]。
# 输入的数组可能包含重复元素 ，所以升序的意思是<=。
#
#
#

"""
public class Solution {
    public int findUnsortedSubarray(int[] nums) {
        Stack < Integer > stack = new Stack < Integer > ();
        int l = nums.length, r = 0;
        for (int i = 0; i < nums.length; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] > nums[i])
                l = Math.min(l, stack.pop());
            stack.push(i);
        }
        stack.clear();
        for (int i = nums.length - 1; i >= 0; i--) {
            while (!stack.isEmpty() && nums[stack.peek()] < nums[i])
                r = Math.max(r, stack.pop());
            stack.push(i);
        }
        return r - l > 0 ? r - l + 1 : 0;
    }
}
"""


class Solution:
    def findUnsortedSubarray(self, nums):
        # 排序法复杂度nlogn, 简洁
        diff = [i for i, (a, b) in enumerate(zip(nums, sorted(nums))) if a != b]
        return len(diff) and max(diff) - min(diff) + 1


if __name__ == "__main__":
    s = Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
    print(s)
    s = Solution().findUnsortedSubarray([2, 6])
    print(s)
    s = Solution().findUnsortedSubarray([2, 6, 1])
    print(s)
    # s = Solution().findUnsortedSubarray([2])
    # print(s)
    # s = Solution().findUnsortedSubarray([2, 1])
    # print(s)

