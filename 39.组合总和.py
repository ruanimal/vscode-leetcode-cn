#
# @lc app=leetcode.cn id=39 lang=python
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (66.21%)
# Likes:    315
# Dislikes: 0
# Total Accepted:    25.4K
# Total Submissions: 38.3K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
#
#
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
#
#
# 示例 2:
#
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
#
#
class SolutionV1(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []

        candidates.sort()
        res = []
        path = []
        self.dfs(candidates, 0, target, path, res)
        return res

    def dfs(self, candidates, begin_level, target, path, res):
        if target == 0:
            res.append(path[:])
        for level in range(begin_level, len(candidates)):
            next_target = target - candidates[level]
            if next_target < 0:
                break
            path.append(candidates[level])
            self.dfs(candidates, level, next_target, path, res)
            path.pop()

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def bt(res, path, t):
            if t == 0:
                res.append(path[:])
                return
            for i in candidates:
                if (not path or path[-1] <= i) and t-i >= 0:
                    path.append(i)
                    bt(res, path, t-i)
                    path.pop()

        if not candidates:
            return []
        res = []
        bt(res, [], target)
        return res


if __name__ == "__main__":
    s = Solution().combinationSum(candidates=[2, 3, 6, 7], target=7)
    print(s)
    s = Solution().combinationSum(candidates=[2, 3, 5], target=8)
    print(s)

