#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (64.36%)
# Likes:    1025
# Dislikes: 0
# Total Accepted:    301K
# Total Submissions: 466.5K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
#
#
# 示例 2：
#
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
#
#
#

from comm import *
# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums):
            if len(track) == len(nums):
                ans.append(track[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                track.append(nums[i])
                used[i] = True
                backtrack(nums)
                used[i] = False
                track.pop()

        ans = []
        track = []
        used = [False] * len(nums)
        backtrack(sorted(nums))
        return ans

# @lc code=end

ans = Solution().permuteUnique(nums = [1,1,2])
print(ans)
