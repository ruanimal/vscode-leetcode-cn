#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#
# https://leetcode-cn.com/problems/flipping-an-image/description/
#
# algorithms
# Easy (79.48%)
# Likes:    276
# Dislikes: 0
# Total Accepted:    92.6K
# Total Submissions: 116.6K
# Testcase Example:  '[[1,1,0],[1,0,1],[0,0,0]]'
#
# 给定一个 n x n 的二进制矩阵 image ，先 水平 翻转图像，然后 反转 图像并返回 结果 。
#
# 水平翻转图片就是将图片的每一行都进行翻转，即逆序。
#
#
# 例如，水平翻转 [1,1,0] 的结果是 [0,1,1]。
#
#
# 反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。
#
#
# 例如，反转 [0,1,1] 的结果是 [1,0,0]。
#
#
#
#
# 示例 1：
#
#
# 输入：image = [[1,1,0],[1,0,1],[0,0,0]]
# 输出：[[1,0,0],[0,1,0],[1,1,1]]
# 解释：首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
# ⁠    然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
#
#
# 示例 2：
#
#
# 输入：image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# 输出：[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 解释：首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
# ⁠    然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
#
#
#
#
# 提示：
#
#
#
#
# n == image.length
# n == image[i].length
# 1 <= n <= 20
# images[i][j] == 0 或 1.
#
#
#

from comm import *
# @lc code=start
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        """暴力法
        可用双指针优化
        """

        image = [row[::-1] for row in image]

        for i in range(len(image)):
            for j in range(len(image[i])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image

if __name__ == "__main__":
    d = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    s = Solution().flipAndInvertImage(d)
    print(s)
# @lc code=end

