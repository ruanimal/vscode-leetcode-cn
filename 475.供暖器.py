#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#
# https://leetcode-cn.com/problems/heaters/description/
#
# algorithms
# Easy (26.06%)
# Total Accepted:    2.1K
# Total Submissions: 8.1K
# Testcase Example:  '[1,2,3]\n[2]'
#
# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
#
# 现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。
#
# 所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。
#
# 说明:
#
#
# 给出的房屋和供暖器的数目是非负数且不会超过 25000。
# 给出的房屋和供暖器的位置均是非负数且不会超过10^9。
# 只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
# 所有供暖器都遵循你的半径标准，加热的半径也一样。
#
#
# 示例 1:
#
#
# 输入: [1,2,3],[2]
# 输出: 1
# 解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
#
#
# 示例 2:
#
#
# 输入: [1,2,3,4],[1,4]
# 输出: 1
# 解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
#
#
#


from comm import *
# @lc code=start


class Solution:
    def findRadius(self, houses: list, heaters: list) -> int:
        """分查找法

        每个节点用的是距离最近的供暖器, 则最大距离就是供暖器的半径
        """
        def binary_search(nums, target):
            """求小于等于target的最大数"""

            left = 0
            right = len(nums)-1
            while left <= right:
                mid = (left+right) >> 1
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        if not houses or not heaters:
            return
        heaters.sort()
        # houses.sort()
        res = 0
        for i in houses:
            h = binary_search(heaters, i)
            # print(i, h)
            if h == -1:   # 所有都大于i
                distance = abs(i - heaters[0])
            elif h == len(heaters)-1:
                distance = abs(i - heaters[-1])
            else:
                distance = min(abs(i-heaters[h]), abs(i-heaters[h+1]))
            res = max(distance, res)
        return res

# @lc code=end

if __name__ == "__main__":
    s = Solution().findRadius([1,2,3,4],[1,4])
    print(s)
