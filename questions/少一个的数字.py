"""
一个数字数组， 只有一个数字出现了2次，其他都出现了3次
"""

def solution(nums):
    bits = [0 for _ in range(32)]
    for num in nums:
        i = 31
        while num > 0:
            if num & 1 == 1:
                bits[i] += 1
            num >>= 1
            i -= 1
    ans = 0
    for i in range(32):
        ans <<= 1
        if (bits[i] % 3) != 0:
            ans |= 1
    return ans


if __name__ == "__main__":
    print(solution([1,5,3,3,3,1,1]))
