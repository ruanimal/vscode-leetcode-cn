'''
给你两个长度相等的整数数组，返回下面表达式的最大值：

|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

其中下标 i，j 满足 0 <= i, j < arr1.length。



示例 1：

输入：arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
输出：13
示例 2：

输入：arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
输出：20


提示：

2 <= arr1.length == arr2.length <= 40000
-10^6 <= arr1[i], arr2[i] <= 10^6
'''

class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        pass

    def maxAbsValExpr2(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int

        暴力法, 超时
        """
        from itertools import permutations
        if len(arr1) <= 1:
            return 0

        ans = 0
        for i, j in permutations(list(range(len(arr1))), 2):
            ans = max(ans, abs(arr1[i]-arr1[j]) + abs(arr2[i]-arr2[j]) + abs(i-j))
        return ans

if __name__ == "__main__":
    s = Solution().maxAbsValExpr(arr1 = [1,2,3,4], arr2 = [-1,4,5,6])
    print(s)
