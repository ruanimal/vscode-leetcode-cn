
data = {1: 5, 2:5, 3:5}
path = []
res = []

def solve(data, target):
    print(''.join(path), 'a', data, target, res)
    if target == 0:
        print(''.join(path), 'd', data, target, res)
        return
    for i in range(1,4):
        if i <= target and data[i] > 0:
            data[i] -= 1
            print(''.join(path), 'b', data, target, res)
            res.append(i)
            path.append('\t')
            solve(data, target-i)
            path.pop()
            res.pop()
            print(''.join(path), 'c', data, target, res)
            data[i] += 1


solve(data, 4)


need = can_stop = collect_result = get_all_choices = set_state = process = revert_state = lambda *args, **kw: args

def backtracking(args):
    if can_stop(args):  # 判断是否终止，限制了递归深度
        if need():   # 必要时收集叶子节点的结果
            collect_result()
        return

    for choice in get_all_choices(args):  # 针对每一种情况, 情况的个数也就是每一层的广度
        set_state(args, choice)  # 暂时选择该项
        res = process(args)   # 该节点数据加工
        if need():   # 必要时该节点的结果
            collect_result()
        backtracking(args)   # 递归进入下一层次
        revert_state(args, choice)   # 撤销当前选择
