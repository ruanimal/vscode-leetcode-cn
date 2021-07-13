
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
