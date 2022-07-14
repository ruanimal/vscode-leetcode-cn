"""
https://labuladong.github.io/algo/3/26/95/
https://juejin.cn/post/6856374004421722125
"""


from typing import List

CHARSET_SIZE = 256

class KMP:
    def __init__(self, pat: str) -> None:
        self.pat = pat
        self.dp = self.init_dp(pat)

    def init_dp(self, pat: str) -> List[List[int]]:
        M = len(pat)
        dp = [list(0 for _ in range(CHARSET_SIZE)) for _ in pat]
        dp[0][ord(pat[0])] = 1
        pre_j = 0
        # dp[j][c] 代表pat[0]到pat[j-1]已匹配上时, 遇到字符c时, 下一步pat指针移动到什么位置
        for j in range(1, M):
            for c in range(CHARSET_SIZE):
                dp[j][c] = dp[pre_j][c]   # 默认回退到有相同前缀的位置, 有部分匹配上了
            # 当前字符匹配, 前进一步
            dp[j][ord(pat[j])] = j+1
            # 状态 pre_j 总是落后状态 j 一个状态，与 j 具有最长的相同前缀。
            pre_j = dp[pre_j][ord(pat[j])]
        return dp

    def search(self, text: str):
        M = len(self.pat)
        N = len(text)
        j = 0
        for i in range(N):
            j = self.dp[j][ord(text[i])]
            if j == M:
                return i - M + 1
        return -1


def main():
    kmp = KMP('ababc')
    res = kmp.search('abababc')
    print(res)
    res = kmp.search('aba2babc')
    print(res)

if __name__ == '__main__':
    main()
