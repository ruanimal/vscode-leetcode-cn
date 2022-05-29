#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#
# https://leetcode-cn.com/problems/design-hashmap/description/
#
# algorithms
# Easy (64.00%)
# Likes:    300
# Dislikes: 0
# Total Accepted:    77.2K
# Total Submissions: 120.9K
# Testcase Example:  '["MyHashMap","put","put","get","get","put","get","remove","get"]\n' +
#   '[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]'
#
# 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
#
# 实现 MyHashMap 类：
#
#
# MyHashMap() 用空映射初始化对象
# void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key
# 已经存在于映射中，则更新其对应的值 value 。
# int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
# void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
#
#
#
#
# 示例：
#
#
# 输入：
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# 输出：
# [null, null, null, 1, -1, null, 1, null, -1]
#
# 解释：
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]]
# myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
# myHashMap.get(1);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
# myHashMap.get(3);    // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
# myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
# myHashMap.get(2);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
# myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
# myHashMap.get(2);    // 返回 -1（未找到），myHashMap 现在为 [[1,1]]
#
#
#
#
# 提示：
#
#
# 0 <= key, value <= 10^6
# 最多调用 10^4 次 put、get 和 remove 方法
#
#
#

# @lc code=start
class MyHashMap:

    def __init__(self):
        self.data = [None] * 10001


    def put(self, key: int, value: int) -> None:
        hash_key = key // 100
        pair = self.data[hash_key]
        if pair is None:
            self.data[hash_key] = (key, value)
        elif isinstance(pair, tuple):
            if pair[0] == key:
                self.data[hash_key] = (key, value)
            else:
                self.data[hash_key] = [pair, (key, value)]
        else:
            for i in range(len(pair)):
                if pair[i][0] == key:
                    pair[i] = (key, value)
                    return
            pair.append((key, value))

    def get(self, key: int) -> int:
        hash_key = key // 100
        pair = self.data[hash_key]
        if pair is None:
            return -1
        elif isinstance(pair, tuple):
            if pair[0] == key:
                return pair[1]
        else:
            for i in pair:
                if i[0] == key:
                    return i[1]
        return -1


    def remove(self, key: int) -> None:
        hash_key = key // 100
        pair = self.data[hash_key]
        if pair is None:
            return
        elif isinstance(pair, tuple):
            if pair[0] == key:
                self.data[hash_key] = None
        else:
            for i in range(len(pair)):
                if pair[i][0] == key:
                    del pair[i]
                    return
        return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

