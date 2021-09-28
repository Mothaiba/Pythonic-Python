b = 5

def f1():
    global b
    print(b)
    b = 100

f1()  # output: 5
print(b)  # output: 100


def f2():
    print(b)
    b = 200

f2()  # output: UnboundLocalError: local variable 'b' referenced before assignment
