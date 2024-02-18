"""
E-mail validation is a widely known problem with several widely known solutions. However, you are working on an advanced spam-detection feature and you don't just need to check that some e-mail is correct, you need to count the number of correct e-mails that can be obtained using the given pattern.

Assume that a correct e-mail is a string satisfying the following conditions:

the string has exactly one character '@' in it;
the string before '@' consists of one or more non-empty groups of lowercase letters from 'a' to 'e' inclusive, separated by '.';
the string after '@' consists of two or more non-empty groups of lowercase letters from 'a' to 'e' inclusive, separated by '.'.
For example,

"a@b.e"
"abcde.edcba@a.b.c.d.e"
are correct e-mails, while those listed below are not:

"@a.a" (no non-empty groups of lowercase letters before '@')
"a@a" (only one non-empty group of lowercase letters after '@')
"a.b@c.d@e.e" (more than one '@' character)
"aa..aa@a.a" (no lowercase letters between two consecutive '.'s)
"abc@d.e.f" ('f' does not belong to the range ['a'..'e'])
"abc.@a.a" (no letters between '.' and '@')
"abc@a.a." (no letters after the last '.')
Example

For pattern = "abcd@?bcd.ca", the output should be
solution(pattern) = 5.

The correct e-mails that may be obtained from this pattern are:

"abcd@abcd.ca"
"abcd@bbcd.ca"
"abcd@cbcd.ca"
"abcd@dbcd.ca"
"abcd@ebcd.ca"
Input/Output

[execution time limit] 4 seconds (py3)

[input] string pattern

An e-mail pattern consisting of lowercase letters and symbols '?', '.' and '@'.

Guaranteed constraints:
5 ≤ pattern.length ≤ 15.

[output] integer

The number of correct e-mails that can be obtained by replacing all '?' with lowercase letters, '.' or '@'.

Input:
pattern: "??????????"
Expected Output:
11562500

"""


import re

def solution_bak(pattern):
    def backtrace(idx):
        if idx == len(indexes):
            if is_valid(''.join(path)):
                ans[0] += 1
            return

        for c in 'abcde@.':
            pre = path[indexes[idx]]
            path[indexes[idx]] = c
            backtrace(idx+1)
            path[indexes[idx]] = pre

    ans = [0]
    path = list(pattern)
    indexes = [i for i, c in enumerate(pattern) if c == '?']
    backtrace(0)
    return ans[0]

def solution(pattern):
    def backtrace(idx):
        if idx == len(indexes):
            if is_valid(''.join(path)):
                # print(''.join(path))
                return 1
            return 0

        ans = 0
        for c in 'a@.':
            pre = path[indexes[idx]]
            path[indexes[idx]] = c
            if c == 'a':
                ans += backtrace(idx+1) * 5
            else:
                ans += backtrace(idx+1)
            path[indexes[idx]] = pre
        return ans

    path = list(pattern)
    indexes = [i for i, c in enumerate(pattern) if c == '?']
    return backtrace(0)

def is_valid(email: str) -> bool:
    p = r'^([a-e]+\.)?([a-e]+)@([a-e]+\.)+([a-e]+)$'
    return re.match(p, email)



assert solution("??????????") == 11562500
