
# 全排列
def permutations(n, k):
    def bt(res, path, used, k):
        if k == 0:
            res.append(path[:])
            return
        for i in range(1, n+1):
            if i not in used:
                used.add(i)
                path.append(i)
                bt(res, path, used, k-1)
                path.pop()
                used.remove(i)

    res = []
    bt(res, [], set(), k)
    return res

print(partition(4, 2))
