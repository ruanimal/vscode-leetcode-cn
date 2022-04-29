"""二分查找"""

def solution(nums, target):
    if not nums:
        return
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1

def findFirst(nums, target):
    """求重复数组的命中的第一个
    可以改造成求 <= target 的最大数
    """

    if not nums:
        return

    left = 0
    right = len(nums) - 1
    while left <= right:   # 取等号保证找到第一个的时候还会继续移动
        print('=', left, right)
        mid = (left + right) >> 1
        if nums[mid] >= target:   # 相等时right左移
            right = mid - 1
        else:
            left = mid + 1
    print(left, right)
    if left == len(nums):   # nums都比target小
        return -1
    if nums[left] != target:
        return -1
    return left

def findLast(nums, target):
    """求重复数组的命中的最后一个
    可以改造成求 >= target 的最小数
    """

    if not nums:
        return

    left = 0
    right = len(nums) - 1
    while left <= right:   # 取等号保证找到第一个的时候还会继续移动
        mid = (left + right) >> 1
        if nums[mid] <= target:   # 相等时left右移, 此时右边界的值的准确的
            left = mid + 1
        else:
            right = mid - 1
    print(left, right)
    if right == -1:   # nums都比target大
        return -1
    if nums[right] != target:
        return -1
    return right

def test():
    assert findFirst([1,3,4,5,7,8,8,8,8,9], 10) == -1
    assert findFirst([1,3,4,5,7,8,8,8,8,9], 8) == 5
    assert findFirst([1,3,4,5,7,8,8,8,8,9], 5.5) == -1
    assert findFirst([1,3,4,5,7,8,8,8,8,9], 0) == -1
    assert findFirst([9,9,9,9,9,9,9,9,9,9], 9) == 0

    assert findLast([1,3,4,5,7,8,8,8,8,9], 10) == -1
    assert findLast([1,3,4,5,7,8,8,8,8,9], 8) == 8
    assert findLast([1,3,4,5,7,8,8,8,8,9], 5.5) == -1
    assert findLast([1,3,4,5,7,8,8,8,8,9], 0) == -1

if __name__ == '__main__':
    test()
