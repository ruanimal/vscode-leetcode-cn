"""命令模式
将请求转换为一个包含与请求相关的所有信息的独立对象。
支持操作历史管理以及撤销操作
"""

import os
from typing import List

class FileOp:
    def execute(self):
        pass

    def undo(self):
        pass

class RenameFile(FileOp):
    def __init__(self, path_src, path_dest):
        self.src = path_src
        self.dest = path_dest

    def execute(self):
        print("[renaming '{}' to '{}']".format(self.src, self.dest))
        os.rename(self.src, self.dest)

    def undo(self):
        print("[renaming '{}' back to '{}']".format(self.dest, self.src))
        os.rename(self.dest, self.src)


class CreateFile(FileOp):
    def __init__(self, path, txt='hello world\n'):
        self.path = path
        self.txt = txt

    def execute(self):
        print("[creating file '{}']".format(self.path))
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)

    def undo(self):
        delete_file(self.path)


class ReadFile(FileOp):
    def __init__(self, path):
        self.path = path

    def execute(self):
        print("[reading file '{}']".format(self.path))
        with open(self.path, mode='r', encoding='utf-8') as in_file:
            print(in_file.read(), end='')


def delete_file(path):
    print("deleting file '{}'".format(path))
    os.remove(path)


def main():
    orig_name, new_name = 'file1', 'file2'

    commands: List[FileOp] = [CreateFile(orig_name), ReadFile(orig_name), RenameFile(orig_name, new_name)]

    for c in commands:
        c.execute()

    answer = input('reverse the executed commands? [y/n] ')

    if answer not in 'yY':
        print("the result is {}".format(new_name))
        exit()

    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            pass

if __name__ == '__main__':
    main()
