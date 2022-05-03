#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (43.59%)
# Likes:    459
# Dislikes: 0
# Total Accepted:    17.7K
# Total Submissions: 39.8K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
#
#
class SolutionB(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        """
        将每一个位置想象成一个桶, 桶的左右边界分别为 往左看的最大值和往右看的最大值,
        桶的理想容量为这两者中较小的那个
        实际容量为, 理想容量 - 桶底的高度
        """

        if not height:
            return 0

        right_maxs = [0 for _ in range(len(height))]    # 右侧最大值
        right_maxs[-1] = height[-1]

        for i in range(len(height)-2, -1, -1):
            right_maxs[i] = max(height[i], right_maxs[i+1])

        ans = 0
        left_max = height[0]    # 左侧最大值
        for i in range(1, len(height)):
            limit = min(left_max, right_maxs[i])   # 理想容量
            space = limit - height[i]   # 实际容量
            if space > 0:
                ans += space
            left_max = max(left_max, height[i])
        return ans

class SolutionA(object):
    def trap(self, height):
        """
        使用栈的解法, LeetCode官方答案, 不好理解

        直观想法

        我们可以不用像方法 2 那样存储最大高度，而是用栈来跟踪可能储水的最长的条形块。使用栈就可以在一次遍历内完成计算。

        我们在遍历数组时维护一个栈。如果当前的条形块小于或等于栈顶的条形块，我们将条形块的索引入栈，意思是当前的条形块被栈中的前一个条形块界定。如果我们发现一个条形块长于栈顶，我们可以确定栈顶的条形块被当前条形块和栈的前一个条形块界定，因此我们可以弹出栈顶元素并且累加答案到ans 。

        """
        if not height:
            return 0
        ans = 0
        current = 0
        st = []
        while current < len(height):
            while st and height[current] > height[st[-1]]:
                print(st, current)
                top = st.pop()
                if not st:
                    break
                distance = current - st[-1] - 1
                bounded_height = min(height[current], height[st[-1]]) - height[top]
                ans += distance * bounded_height
            st.append(current)
            current += 1
        return ans

class Solution(object):
    def trap(self, height):
        """双指针法"""

        if not height:
            return 0
        ans = 0
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        while left < right:
            if height[left] < height[right]:   # 以小的那边为桶的高
                if height[left] >= left_max:
                    left_max = height[left]   # 更新左最大值
                else:
                    ans += (left_max - height[left])
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += (right_max - height[right])
                right -= 1
        return ans

# @lc code=end


if __name__ == "__main__":
    s = SolutionA().trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print(s)
    s = SolutionB().trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print(s)
    s = Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print(s)


