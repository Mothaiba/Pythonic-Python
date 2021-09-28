from collections import abc

print(issubclass(abc.Iterator, abc.Iterable))  # output: True


def gen_12():
    yield 1
    yield 2


g = gen_12()
print(next(g))  # output: 1
print(next(g))  # output: 2
print(next(g))  # output: Traceback ... StopIteration
