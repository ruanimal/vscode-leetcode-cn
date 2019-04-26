#
# @lc app=leetcode.cn id=944 lang=python
#
# [944] 最小差值 I
#
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        D = []
        for y in range(len(A[0])):
            pre = A[0][y]
            for x in range(1, len(A)):
                if A[x][y] < pre:
                    D.append(y)
                    break
                pre = A[x][y]
        # print(D)
        return len(D)

if __name__ == "__main__":
    s = Solution().minDeletionSize(["cba", "daf", "ghi"])
    print(s)
    s = Solution().minDeletionSize(["abcdef", "uvwxyz"])
    print(s)
    s = Solution().minDeletionSize(["rrjk",
                                    "furt",
                                    "guzm"])
    print(s)

