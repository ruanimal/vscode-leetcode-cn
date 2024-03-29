#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#
# https://leetcode-cn.com/problems/design-hashset/description/
#
# algorithms
# Easy (63.94%)
# Likes:    236
# Dislikes: 0
# Total Accepted:    84.7K
# Total Submissions: 132.6K
# Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n' +
#   '[[],[1],[2],[1],[3],[2],[2],[2],[2]]'
#
# 不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
#
# 实现 MyHashSet 类：
#
#
# void add(key) 向哈希集合中插入值 key 。
# bool contains(key) 返回哈希集合中是否存在这个值 key 。
# void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
#
#
#
# 示例：
#
#
# 输入：
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains",
# "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# 输出：
# [null, null, null, true, false, null, true, null, false]
#
# 解释：
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // 返回 True
# myHashSet.contains(3); // 返回 False ，（未找到）
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // 返回 True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // 返回 False ，（已移除）
#
#
#
# 提示：
#
#
# 0 <= key <= 10^6
# 最多调用 10^4 次 add、remove 和 contains
#
#
#

# @lc code=start
class MyHashSet:
    """拉链法
    有优化空间, 拉链用链表实现
    """

    def __init__(self):
        self.data = [None] * 10001

    def add(self, key: int) -> None:
        value = 1
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


    def remove(self, key: int) -> None:
        hash_key = key // 100
        pair = self.data[hash_key]
        # print(pair)
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

    def contains(self, key: int) -> bool:
        hash_key = key // 100
        pair = self.data[hash_key]
        if pair is None:
            return False
        elif isinstance(pair, tuple):
            if pair[0] == key:
                return True
        else:
            for i in pair:
                if i[0] == key:
                    return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

