#
# @lc app=leetcode.cn id=1002 lang=python
#
# [1002] 最大宽度坡
#
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        if len(A) == 1:
            return list(A[0])

        counts = []
        for s in A:
            t = {}
            for i in s:
                t[i] = t.get(i, 0) + 1
            counts.append(t)
        tmp = {}
        for i in 'abcdefghijklmnopqrstuvwxyz':
            tmp[i] = 100  # max value
            for count in counts:
                if i not in count:
                    tmp[i] = 0
                    break
                tmp[i] = min(tmp[i], count[i])
        ret = []
        for k, v in tmp.items():
            for _ in range(v):
                ret.append(k)
        return ret

if __name__ == "__main__":
    s = Solution().commonChars(["bella","label","roller"])
    print(s)
    s = Solution().commonChars(["cool","lock","cook"])
    print(s)

