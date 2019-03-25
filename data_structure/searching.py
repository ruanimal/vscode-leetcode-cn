def linear_search(array, k):
    if not array:
        return -1
    for i in range(len(array)):
        if array[i] < k:
            continue
        elif array[i] > k:
            return -1
        else:
            return i


def binary_search(array, k, left=None, right=None):
    """递归版本, 比较循环慢50%"""
    if not array:
        return -1
    if left is None and right is None:
        left = 0
        right = len(array) -1

    mid = (right + left) // 2
    if k < array[left]:
        return -1
    elif array[left] == k:
        return left
    elif k < array[mid]:
        return binary_search(array, k, left, mid)
    elif k == array[mid]:
        return mid
    elif k < array[right]:
        return binary_search(array, k, mid+1, right)
    elif array[right] == k:
        return right
    else:
        return -1

def binary_search_loop_version(array, k):
    left = 0
    right = len(array) -1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == k:
            return mid
        elif array[mid] > k:
            right = mid -1
        else:
            left = mid + 1
    return -1


if __name__ == "__main__":
    l = list(range(20))
    print(linear_search(l, 11))
    print(binary_search(l, 10))
    print(binary_search_loop_version(l, 10))
