#
# @lc app=leetcode.cn id=788 lang=python
#
# [788] 旋转数字
#
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        # # ????
        # cnt = 0
        # for i in range(1, N+1):
        #     i = str(i)
        #     if '3' in i or '4' in i or '7' in i:
        #         continue
        #     if '2' not in i and '5' not in i and '6' not in i and '9' not in i:
        #         continue
        #     cnt += 1
        # return cnt

        count = 0
        trans_map = {'1':'1', '0':'0', '8':'8', '2': '5', '5': '2', '6': '9', '9': '6'}
        for i in range(1, N+1):
            str_num = list(str(i))
            tmp = []
            for j in str_num:
                if j in trans_map:
                    tmp.append(trans_map[j])
                else:
                    break
            if len(tmp) == len(str_num) and tmp != str_num:
                count += 1
        return count

if __name__ == "__main__":
    s = Solution().rotatedDigits(10)
    print(s)

