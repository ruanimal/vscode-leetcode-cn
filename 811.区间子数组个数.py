#
# @lc app=leetcode.cn id=811 lang=python
#
# [811] 区间子数组个数
#
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        ret_map = {}
        for i in cpdomains:
            nums, domains = i.split()
            domains = domains.split('.')
            for idx in range(len(domains)-1, -1, -1):
                key = '.'.join(domains[idx:])
                ret_map[key] = ret_map.get(key, 0) + int(nums)
        return ['{} {}'.format(v, k) for k, v in ret_map.items()]

if __name__ == "__main__":
    s = Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
    print(s)
