#
# @lc app=leetcode.cn id=18 lang=python
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (35.95%)
# Likes:    271
# Dislikes: 0
# Total Accepted:    30K
# Total Submissions: 83.5K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 
# 注意：
# 
# 答案中不可以包含重复的四元组。
# 
# 示例：
# 
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 
# 满足要求的四元组集合为：
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
            
        nums.sort()
        ans = set()
        route = []
        self.helper(0, nums, target, ans, route)
        return list(list(i) for i in ans) 

    @staticmethod
    def helper(index, nums, target, ans, route):
        if index >= len(nums):
            if target == 0 and len(route) == 4:
                ans.add(tuple(route))
            return 
        # print(index, nums, target, ans, route)
        route.append(nums[index])
        Solution.helper(index+1, nums, target-nums[index], ans, route)
        route.pop()
        Solution.helper(index+1, nums, target, ans, route)
        
if __name__ == "__main__":
    s = Solution().fourSum(nums = [1, 0, -1, 0, -2, 2], target = 0)
    print(s)

