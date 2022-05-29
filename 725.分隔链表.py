#
# @lc app=leetcode.cn id=725 lang=python3
#
# [725] 分隔链表
#
# https://leetcode-cn.com/problems/split-linked-list-in-parts/description/
#
# algorithms
# Medium (47.85%)
# Total Accepted:    1.3K
# Total Submissions: 2.7K
# Testcase Example:  '[1,2,3,4]\n5'
#
# 给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。
#
# 每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。
#
# 这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。
#
# 返回一个符合上述规则的链表的列表。
#
# 举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]
#
# 示例 1：
#
#
# 输入:
# root = [1, 2, 3], k = 5
# 输出: [[1],[2],[3],[],[]]
# 解释:
# 输入输出各部分都应该是链表，而不是数组。
# 例如, 输入的结点 root 的 val= 1, root.next.val = 2, \root.next.next.val = 3, 且
# root.next.next.next = null。
# 第一个输出 output[0] 是 output[0].val = 1, output[0].next = null。
# 最后一个元素 output[4] 为 null, 它代表了最后一个部分为空链表。
#
#
# 示例 2：
#
#
# 输入:
# root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
# 输出: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# 解释:
# 输入被分成了几个连续的部分，并且每部分的长度相差不超过1.前面部分的长度大于等于后面部分的长度。
#
#
#
#
# 提示:
#
#
# root 的长度范围： [0, 1000].
# 输入的每个节点的大小范围：[0, 999].
# k 的取值范围： [1, 50].
#
#
#
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from comm import *
# @lc code=start

class Solution(object):
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        """模拟发扑克牌
        写得比较啰嗦, 有优化空间
        """

        if not root:
            return [None] * k

        # 求总长度
        count = 0
        ptr = root
        while ptr:
            count += 1
            ptr = ptr.next

        # 计算每部分大小
        s, y = divmod(count, k)
        count_part = [s] * k
        i = 0
        while y > 0:
            if i == k:
                i = 0
            count_part[i] += 1
            i += 1
            y -= 1

        ret = []
        ptr = root
        for pre_part in count_part:
            ret.append(ptr)
            for _ in range(pre_part-1):
                if not ptr.next:
                    break
                ptr = ptr.next
            if not ptr.next:
                break
            tmp = ptr.next
            ptr.next = None
            ptr = tmp
        ret.extend([None]*(k-len(ret)))
        return ret

# @lc code=end

if __name__ == "__main__":
    l = build_list_node(range(4))
    print(Solution().splitListToParts(l, 5))
