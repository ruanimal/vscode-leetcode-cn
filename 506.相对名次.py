#
# @lc app=leetcode.cn id=506 lang=python
#
# [506] 相对名次
#
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranks_map = {num: str(idx+1) for idx, num in enumerate(sorted(nums, reverse=True))}
        medels = {
            "1": "Gold Medal",
            "2": "Silver Medal",
            "3": "Bronze Medal",
        }
        return [medels.get(ranks_map[i], ranks_map[i]) for i in nums]

if __name__ == "__main__":
    s = Solution().findRelativeRanks([5, 4, 3, 2, 1])
    print(s)
