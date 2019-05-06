#
# @lc app=leetcode.cn id=806 lang=python
#
# [806] 写字符串需要的行数
#
class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        widths_map = dict(zip('abcdefghijklmnopqrstuvwxyz', widths))
        length = 0
        for i in S:
            if (length + widths_map[i]) > (length // 100 + 1) * 100:
                length = (length // 100 + 1) * 100
            length += widths_map[i]
        a, b = divmod(length, 100)
        if b:
            return [a + 1, b]
        return a, b


if __name__ == "__main__":
    s = Solution().numberOfLines(widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], S = "bbbcccdddaaa")
    print(s)
    s = Solution().numberOfLines(widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], S = "abcdefghijklmnopqrstuvwxyz")
    print(s)

