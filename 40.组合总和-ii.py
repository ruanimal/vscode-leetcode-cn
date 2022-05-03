#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (61.10%)
# Likes:    926
# Dislikes: 0
# Total Accepted:    277.5K
# Total Submissions: 456.3K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用 一次 。
#
# 注意：解集不能包含重复的组合。 
#
#
#
# 示例 1:
#
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
# 示例 2:
#
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]
#
#
#
# 提示:
#
#
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
#
#
#

from comm import *
# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(nums, idx, total):
            if total == target:
                ans.append(track[:])
                return
            if total > target:  # 剪枝,降低复杂度
                return
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:  # 剪枝,去重
                    continue
                total += nums[i]
                track.append(nums[i])
                backtrack(nums, i+1, total)
                track.pop()
                total -= nums[i]

        ans = []
        track = []
        backtrack(sorted(candidates), 0, 0)
        return ans

# @lc code=end

ans = Solution().combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8,)
print(ans)
