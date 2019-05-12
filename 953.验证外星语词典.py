#
# @lc app=leetcode.cn id=953 lang=python
#
# [953] 验证外星语词典
#
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        order_map = dict((i, idx) for idx, i in enumerate(order))
        i = 0
        while i < len(words)-1:
            a, b = words[i], words[i+1]
            j = 0
            while j < 20:
                if j < len(a) and j < len(b):
                    if order_map[a[j]] < order_map[b[j]]:
                        break
                    elif order_map[a[j]] > order_map[b[j]]:
                        return False
                    else:
                        j += 1
                        continue
                elif j >= len(a) and j >= len(b):
                    break
                elif j >= len(a):
                    break
                else:
                    return False
            i += 1
        return True

if __name__ == "__main__":
    s = Solution().isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz")
    print(s)
    s = Solution().isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz")
    print(s)
    # import ipdb; ipdb.set_trace()
    s = Solution().isAlienSorted(["ubg","kwh"], "qcipyamwvdjtesbghlorufnkzx")
    print(s)
