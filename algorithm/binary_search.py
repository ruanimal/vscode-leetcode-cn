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

def solution2(nums, target):
    """求小于等于target的数"""

    if not nums:
        return
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) >> 1
        if nums[mid] < target:
            left = mid + 1   # target 不可能在 (mid, right] 中, 则下一轮区间不包含mid
        else:
            right = mid  # target 可能在 [left, mid] 中, 则下一轮区间包含mid
    # 最终 (nums[left] == nums[right]) >= target, 因为只要nums[mid] < target就会再进一步
    if nums[left] == target:
        return left
    return left - 1

if __name__ == "__main__":
    s = solution([1,3,4,5,7,8], 6)
    print(s)
    s = solution2([1,3,4,5,7,8], 0)
    print(s)
