#
# @lc app=leetcode.cn id=566 lang=python
#
# [566] 重塑矩阵
#
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        flat_nums = sum(nums, [])
        if r * c != len(flat_nums):
            return nums

        ans = []
        for i in range(r):
            tmp = flat_nums[i*c:(i+1)*c]
            ans.append(tmp)
        return ans

if __name__ == "__main__":
    s = Solution().matrixReshape([[1,2], [3,4]], r = 2, c = 4)
    print(s)

