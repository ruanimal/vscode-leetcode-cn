import json
from copy import deepcopy
import bz2
import msgpack


class TrieTree:
    def __init__(self, cache=None, sep='|'):
        if cache is None:
            cache = {}
        assert isinstance(cache, dict)
        self._cache = deepcopy(cache)
        self.sep = sep

    @classmethod
    def from_json(cls, string: str, sep='|'):
        return TrieTree(json.loads(string), sep)

    def to_json(self) -> str:
        return json.dumps(self._cache)

    def batch_insert(self, words: str) -> None:
        for word in words:
            self.insert(word)

    def insert(self, word: str) -> None:
        cache = self._cache
        for i in word.split(self.sep):
            cache = cache.setdefault(i, {})
        cache['#'] = 1

    def search(self, word: str) -> bool:
        cache = self._cache
        for i in word.split(self.sep):
            cache = cache.get(i)
            if cache is None:
                return False
        return cache.get('#', 0) > 0


def test():
    t = TrieTree()
    t.insert('aaa|bc')
    assert t._cache == {'aaa': {'bc': {'#': 1}}}
    t.insert('aaa|bcd')
    assert t._cache == {'aaa': {'bc': {'#': 1}, 'bcd': {'#': 1}}}
    t.insert('ab|bcd')
    assert t._cache == {'aaa': {'bc': {'#': 1}, 'bcd': {'#': 1}}, 'ab': {'bcd': {'#': 1}}}
    # print(t._cache)
    assert t.search('ab') == False
    assert t.search('ab|bcd') == True
    assert t.to_json() == '{"aaa": {"bc": {"#": 1}, "bcd": {"#": 1}}, "ab": {"bcd": {"#": 1}}}'
    t2 = TrieTree.from_json(t.to_json())
    assert t2._cache == t._cache

def compress():
    old = open('/Users/ruan/Downloads/aaa.json').read()
    old = json.loads(old)
    old = [i for i in old if not i.startswith('creditOwnData|manualModelResultList')]
    old = json.dumps(old)
    t = TrieTree()
    t.batch_insert(json.loads(old))
    new = t.to_json()
    print(len(old), len(new),
          len(msgpack.dumps(json.loads(old))),
          len(msgpack.dumps(json.loads(new))),
          len(bz2.compress(old.encode('utf8'), compresslevel=3)), len(bz2.compress(new.encode('utf8'), compresslevel=3)))

compress()
