class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        start_index = 0
        res = ''
        for i in range(len(S)):
            if S[i] == '(':
                stack.append(S[i])
            else:
                stack.pop()
            if not stack:
                res += S[start_index+1:i]
                start_index = i+1
        return res

if __name__ == "__main__":
    s = Solution().removeOuterParentheses("(()())(())(()(()))")
    print(s)

