class Count:
    def __init__(self):
        self.num = 0

    def __call__(self):
        self.num += 1
        return self.num


count = Count()
print(count())  # output: 1
print(count())  # output: 2
print(count())  # output: 3

print(callable(count))  # output: True