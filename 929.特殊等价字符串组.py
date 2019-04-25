#
# @lc app=leetcode.cn id=929 lang=python
#
# [929] 特殊等价字符串组
#
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        ret = set()
        for email in emails:
            at_idx = email.index('@')
            tmp = []
            for idx, i in enumerate(email):
                if i == '.':
                    continue
                if (i == '+' or idx >= at_idx):
                    break
                tmp.append(i)
            tmp.append(email[at_idx:])
            ret.add(''.join(tmp))
        # print(ret)
        return len(ret)

if __name__ == "__main__":
    s = Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
    print(s)
