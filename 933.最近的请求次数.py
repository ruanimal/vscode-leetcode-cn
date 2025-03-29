#
# @lc app=leetcode.cn id=933 lang=python3
#
# [933] 最近的请求次数
#
# https://leetcode-cn.com/problems/number-of-recent-calls/description/
#
# algorithms
# Easy (72.86%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    81.5K
# Total Submissions: 105.7K
# Testcase Example:  '["RecentCounter","ping","ping","ping","ping"]\n[[],[1],[100],[3001],[3002]]'
#
# 写一个 RecentCounter 类来计算特定时间范围内最近的请求。
#
# 请你实现 RecentCounter 类：
#
#
# RecentCounter() 初始化计数器，请求数为 0 。
# int ping(int t) 在时间 t 添加一个新请求，其中 t 表示以毫秒为单位的某个时间，并返回过去 3000
# 毫秒内发生的所有请求数（包括新请求）。确切地说，返回在 [t-3000, t] 内发生的请求数。
#
#
# 保证 每次对 ping 的调用都使用比之前更大的 t 值。
#
#
#
# 示例 1：
#
#
# 输入：
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# 输出：
# [null, 1, 2, 3, 3]
#
# 解释：
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1]，范围是 [-2999,1]，返回 1
# recentCounter.ping(100);   // requests = [1, 100]，范围是 [-2900,100]，返回 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001]，范围是 [1,3001]，返回 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002]，范围是 [2,3002]，返回
# 3
#
#
#
#
# 提示：
#
#
# 1 <= t <= 10^9
# 保证每次对 ping 调用所使用的 t 值都 严格递增
# 至多调用 ping 方法 10^4 次
#
#
#

# @lc code=start


class RecentCounterA:
    """简单实现"""

    def __init__(self):
        self.queue = []

    def ping(self, t):
        self.queue.append(t)

        i = 0
        while i < len(self.queue):
            if(self.queue[i] + 3000 < t):
                i+=1
            else:
                break
        self.queue[:i] = []
        return len(self.queue)


class RecentCounter:
    """环形数组+二分查找
    理论上更快,但是实际不行

    68/68 cases passed (179 ms)
    Your runtime beats 11 % of python3 submissions
    Your memory usage beats 55.08 % of python3 submissions (22.7 MB)
    """
    def __init__(self):
        self.queue = [-9999] * 3001
        self.free_idx = 0
        self.used = 0

    def search(self, target: int) -> int:
        # 找到 >= target
        LEN = len(self.queue)
        i = self.free_idx
        j = LEN + self.free_idx-1
        while i <= j:
            mid = (i+j)>>1
            val = self.queue[mid%LEN]
            # if target == 2-3000:
            #     print('=', mid, val)
            if val == target:
                j = mid-1
            elif val > target:
                j = mid-1
            elif val < target:
                i = mid+1
        # print('+', i, self.queue[i%LEN])
        return i % LEN

    def ping(self, t):
        self.queue[self.free_idx] = t
        self.free_idx = (self.free_idx+1) % len(self.queue)
        if self.used < len(self.queue):
            self.used += 1
        s = self.search(t-3000)
        # print('=', s, self.free_idx, self.queue[s])
        if s < self.free_idx:
            return self.free_idx - s
        return self.used - s + self.free_idx


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

obj = RecentCounter()
for i in [[],[2196],[3938],[4723],[4775],[5952]]:
    if i:
        print(obj.ping(i[0]))
# for i in range(3010):
#     if i < 10 or i > 2999:
#         print(i, obj.ping(i), obj.queue[:5], obj.queue[-5:])
#     else:
#         obj.ping(i)
