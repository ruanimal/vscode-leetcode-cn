'''
1. a, b 两个文件 50亿条url
2. 找出重复的url
'''

import os

PRAT = 500
PER_PART = 5000000000 // PRAT

def handle_file(file_name):
    if not os.path.exists(file_name):
        return
    with open(file_name) as target:
        for line in target:
            yield line


def make_tmpfiles(prefix, part=PRAT):
    fds = []
    for i in range(PRAT):
        fd = open('{}_{}'.format(prefix, i), 'w+')
        fds.append(fd)
    return fds


def solution(a, b):
    parts_a = make_tmpfiles(a)
    parts_b = make_tmpfiles(b)
    ans_file = open('ans.txt', 'w')

    for line in handle_file(a):
        idx = hash(line) % PRAT
        parts_a[idx].write(line)

    for line in handle_file(b):
        idx = hash(line) % PRAT
        parts_b[idx].write(line)

    for fd_a, fd_b in zip(parts_a, parts_b):
        fd_a.seek(0)
        fd_b.seek(0)
        tmp_set = set(i.strip() for i in fd_a)
        for line in fd_b:
            if line.strip() in tmp_set:
                ans_file.write(line)

    for i in parts_a:
        i.close()
        os.remove(i.name)
    for i in parts_b:
        i.close()
        os.remove(i.name)
    ans_file.close()

if __name__ == "__main__":
    solution('a.txt', 'b.txt')
