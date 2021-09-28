def make_averager():
    total = 0
    count = 0

    def averager(v):
        nonlocal total, count
        total += v
        count += 1
        return total / count

    return averager


avg = make_averager()
print(avg(10))  # output: 10
print(avg(20))  # output: 15
print(avg(30))  # output: 20
