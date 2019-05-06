#
# @lc app=leetcode.cn id=821 lang=python
#
# [821] 打砖块
#
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        不能用动态规划， 因为不满足后无效性
        """
        e_indexs = [idx for idx, i in enumerate(S) if i==C]
        # e_indexs.sort()
        ret = []
        for idx, i in enumerate(S):
            # 可用二分查找求最近的e
            ret.append(min(abs(idx-j) for j in e_indexs))
        return ret

if __name__ == "__main__":
    s = Solution().shortestToChar(S = "loveleetcode", C = 'e')
    print(s)

