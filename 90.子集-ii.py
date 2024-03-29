#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (63.41%)
# Likes:    802
# Dislikes: 0
# Total Accepted:    191K
# Total Submissions: 301.1K
# Testcase Example:  '[1,2,2]'
#
# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
#
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#
#
# 示例 2：
#
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
#
#
# 提示：
#
#
# 1
# -10
#
#
#
#
#
from comm import *
# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, idx):
            ans.append(track[:])
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:  # 关键剪枝
                    continue
                track.append(nums[i])
                backtrack(nums, i+1)
                track.pop()

        ans = []
        track = []
        backtrack(sorted(nums), 0)
        return ans

# @lc code=end

ans = Solution().subsetsWithDup([1,2,2])
print(ans)
