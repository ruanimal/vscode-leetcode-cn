#
# @lc app=leetcode.cn id=748 lang=python
#
# [748] 至少是其他数字两倍的最大数
#
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        letter = {}
        for i in licensePlate:
            if i.isalpha():
                i = i.lower()
                letter[i] = letter.get(i, 0) + 1
        letter_len = sum(letter.values())
        ans = None
        for word in words:
            tmp = {}
            for i in word:
                tmp[i] = tmp.get(i, 0) + 1
            for k, v in letter.items():
                if k not in tmp:
                    break
                if tmp[k] < v:
                    break
            else:
                if not ans:
                    ans = word
                if len(word) < len(ans):
                    ans = word
                if len(ans) == letter_len:
                    return ans
        return ans

if __name__ == "__main__":
    s = Solution().shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"])
    print(s)

