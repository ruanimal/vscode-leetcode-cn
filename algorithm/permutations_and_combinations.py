"""
product('ABCD', repeat=2)   # 全排列，元素可重复

AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD

permutations('ABCD', 2)  # 全排列

AB AC AD BA BC BD CA CB CD DA DB DC

combinations('ABCD', 2)  # 组合

AB AC AD BC BD CD

combinations_with_replacement('ABCD', 2)  # 组合元素可重复
"""

# def permutations(iterable, r=None):
#     # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
#     # permutations(range(3)) --> 012 021 102 120 201 210
#     pool = tuple(iterable)
#     n = len(pool)
#     r = n if r is None else r
#     if r > n:
#         return
#     indices = list(range(n))  # [0, 1, 2, 3]
#     cycles = list(range(n, n - r, -1))  # [4, 3] 固定一个元素（4种选择），剩下的元素有3种选择
#     yield tuple(pool[i] for i in indices[:r])   # 取前r个元素
#     while n:
#         for i in reversed(range(r)):  # 代表排列的层次， [1, 0]
#             # cycles[i]， 代表当前这个层次的可能性
#             print('xx', i, cycles)
#             cycles[i] -= 1
#             if cycles[i] == 0:  # 这个层次已经穷举完了
#                 # print('---', indices)
#                 indices[i:] = indices[i + 1:] + indices[i:i + 1]   #
#                 # print('--+', indices)
#                 cycles[i] = n - i
#             else:
#                 j = cycles[i]
#                 indices[i], indices[-j] = indices[-j], indices[i]   # 其他层次不变， 将这个层次的的可能逐次试一下
#                 yield tuple(pool[i] for i in indices[:r])
#                 break
#         else:
#             return


def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))  # [0, 1, 2, 3]
    cycles = list(range(n, n - r, -1))  # [4, 3] 固定一个元素（4种选择），剩下的元素有3种选择
    yield tuple(pool[i] for i in indices[:r])   # 取前r个元素
    while n:
        for i in reversed(range(r)):  # 代表排列的层次， [1, 0]
            # cycles[i]， 代表当前这个层次的可能性
            cycles[i] -= 1
            if cycles[i] == 0:  # 这个层次已经穷举完了
                indices[i:] = indices[i + 1:] + indices[i:i + 1]   #
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]   # 其他层次不变， 将这个层次的的可能逐次试一下
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


def combinations(iterable, r):
    # 4 2
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    for indices in permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)


def combinations_with_replacement(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in product(range(n), repeat=r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)


if __name__ == "__main__":
    print(list(product('ABCD', repeat=2)))
    print(list(combinations_with_replacement('ABCD', 2)))
    print(list(permutations('ABCD', 2)))
    print(list(combinations('ABCD', 2)))
