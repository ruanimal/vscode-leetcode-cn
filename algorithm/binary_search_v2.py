"""二分查找"""


def findFirst(nums, target):
    """求重复数组的命中的第一个
    可以改造成求 大于等于 target 的最小数
    """

    if not nums:
        return

    left = 0
    right = len(nums)
    # 有效区间为[left, right)
    while left < right:
        mid = (left + right) >> 1   # left == right时取左侧边界
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] == target:   # 相等时取左半边, 不含mid这个点
            right = mid
        else:
            right = mid - 1
    print('=', left, right)
    if left == len(nums) or nums[left] != target:   # nums都比target小或不存在
        return -1
    return left

def findLast(nums, target):
    """求重复数组的命中的最后一个
    可以改造成求 小于等于 target 的最大数
    """

    if not nums:
        return

    left = -1
    right = len(nums)-1
    # 有效区间为(left, right]
    while left < right:   # 取等号保证找到第一个的时候还会继续移动
        mid = (left + right + 1) >> 1    # left == right时取右侧边界
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] == target:   # 相等时取右半边, 不含mid这个点
            left = mid
        else:
            right = mid - 1
    print('=', left, right)
    if right == -1 or nums[right] != target:  # nums都比target大或不存在
        return -1
    return right

def test():
    assert findFirst([1,3,4,5,7,8,8,8,8,9], 10) == -1
    assert findFirst([1,3,4,5,7,8,8,8,8,9], 8) == 5
    assert findFirst([1,3,4,5,7,8,8,8,8,9], 5.5) == -1
    assert findFirst([1,3,4,5,7,8,8,8,8,9], 7.5) == -1
    assert findFirst([1,3,4,5,7,8,8,8,8,9], 0) == -1
    assert findFirst([9,9,9,9,9,9,9,9,9,9], 9) == 0

    assert findLast([1,3,4,5,7,8,8,8,8,9], 10) == -1
    assert findLast([1,3,4,5,7,8,8,8,8,9], 8) == 8
    assert findLast([1,3,4,5,7,8,8,8,8,9], 5.5) == -1
    assert findLast([1,3,4,5,7,8,8,8,8,9], 0) == -1
    assert findLast([1,3,4,5,7,8,8,8,8,8], 8) == 9
    assert findLast([9,9,9,9,9,9,9,9,9,9], 9) == 9

if __name__ == '__main__':
    test()
