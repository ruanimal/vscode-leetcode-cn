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

def binary_search(nums, target):
    """常规二分查找, 不支持重复项"""

    if not nums:
        return

    left = 0
    right = len(nums)-1
    # 寻找区间[left, right], 使得 nums[left] <= target <= nums[right], 直到left == right
    while left < right:
        # 当区间大小等于2时, mid == left;
        # - 没到边界的情况下, 如果target不在两者之中, 最终的left取的是右边界, 此时nums[left] >= target
        # - 到左边界时(0), nums[left] >= target
        # - 到右边界时(len(nums)-1), nums[left] <= target
        mid = (left + right) >> 1
        if nums[mid] < target: # 排除掉 [left, mid] 选择[mid+1, right], 此时取值区间 [target, max)
            left = mid + 1
        else:
            right = mid   # 等于target的情况在左半边的结尾
    if nums[left] != target:
        return -1
    return left

def binary_search2(nums, target):
    """常规二分查找, 不支持重复项"""

    if not nums:
        return

    left = 0
    right = len(nums)-1
    while left < right:
        # 注意+1, 也就是区间为2时, 取右边界
        mid = (left + right + 1) >> 1
        if nums[mid] <= target: # 划分区间时将等值放在右半边的开头
            left = mid
        else:
            right = mid - 1
    print(left, right)
    if nums[left] != target:
        return -1
    return left

def findFirst(nums, target):
    """求重复数组的命中的第一个
    可以改造成求 大于等于 target 的最小数
    """

    if not nums:
        return

    left = 0
    right = len(nums) - 1
    while left <= right:   # 取等号保证找到第一个的时候还会继续移动
        # print('=', left, right)
        mid = (left + right) >> 1
        if nums[mid] >= target:   # 相等时right左移
            right = mid - 1
        else:   # target > nums[mid]
            left = mid + 1
    # 退出时 left > right, 更确切地说, left - 1 == right
    # 退出时 nums[left] >= target
    # 由于mid+1 和 mid-1, right可能等于-1, left等于len(nums)
    print(left, right)
    if left == len(nums):   # nums都比target小
        return -1
    if nums[left] != target:
        return -1
    return left

def findLast(nums, target):
    """求重复数组的命中的最后一个
    可以改造成求 小于等于 target 的最大数
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
    assert binary_search2([1,3,4,5,7,8,9], 8) == 5
    assert binary_search2([1,3,4,5,7,8,9], 0) == -1
    assert binary_search2([1,3,4,5,7,8,9], 10) == -1
    return
    assert findFirst([1,3,4,5,7,8,8,8,8,9], 10) == -1
    assert findFirst([1,3,4,5,7,8,8,8,8,9], 8) == 5
    assert findFirst([1,3,4,5,7,8,8,8,8,9], 5.5) == -1
    assert findFirst([1,3,4,5,7,8,8,8,8,9], 7.5) == -1
    assert findFirst([1,3,4,5,7,8,8,8,8,9], 0) == -1
    assert findFirst([9,9,9,9,9,9,9,9,9,9], 9) == 0


    # assert findLast([1,3,4,5,7,8,8,8,8,9], 10) == -1
    # assert findLast([1,3,4,5,7,8,8,8,8,9], 8) == 8
    # assert findLast([1,3,4,5,7,8,8,8,8,9], 5.5) == -1
    # assert findLast([1,3,4,5,7,8,8,8,8,9], 0) == -1

if __name__ == '__main__':
    # test()
    assert findLast([1,3,4,5,7,8,8,8,8,9], 5.5) == -1
