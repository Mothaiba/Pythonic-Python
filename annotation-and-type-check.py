from typing import List


def push(l: List[int], v: int) -> None:
    l.append(v)


my_list: List[int] = []
push(my_list, 5)
print(my_list)

push(my_list, 1.2)
print(my_list)
