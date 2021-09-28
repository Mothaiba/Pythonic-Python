def func(a, *b, c, **kwargs):
    print(a, b, c, kwargs)


func("tung", 10, b=1, c="123")  # output: tung (10,) 123 {'b': 1}
