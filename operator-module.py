from operator import itemgetter


arr = [('b', 1), ('a', 1), ('a', 0)]

# below, itemgetter(1) means the same as lambda x: x[1]
print(sorted(arr, key=itemgetter(1)))  # output: [('a', 0), ('b', 1), ('a', 1)]

# below, itemgetter(1, 0) means the same as lambda x: (x[1], x[0])
print(sorted(arr, key=itemgetter(1, 0)))  # output: [('a', 0), ('a', 1), ('b', 1)]