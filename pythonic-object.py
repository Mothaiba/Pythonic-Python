class Vector2d:
    def __init__(self, x, y):
        self.__vector = (float(x), float(y))

    @classmethod
    def from_string(cls, s):
        x, y = (float(item) for item in s.split())
        return cls(x, y)

    @property
    def x(self):
        return self.__vector[0]

    @property
    def y(self):
        return self.__vector[1]

    def __iter__(self):
        return (v for v in self.__vector)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __str__(self):
        return str(tuple(self))

    def __repr__(self):
        class_name = type(self).__name__
        return "{}({!r}, {!r})".format(class_name, *self)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)  # this is a simple way of hashing.

    def __getitem__(self, i):
        return self.__vector[i]


# below calls the __init__ method
v = Vector2d(3, 4)

# below calls the __iter__ method
x, y = v
print(x, y)  # output: 3.0 4.0

# below calls the __eq__ method
print(v == (3, 4))  # output: True

# below calls the __str__ method
print(v)  # output: (3.0, 4.0)

# below calls the __repr__ method
print(repr(v))  # output: Vector2d(3.0, 4.0)

# below calls the __hash__ method
print(hash(v))  # output: 7

# below calls the __getitem__ method
print(v[1])  # output: 4.0

# below calls the from_string method
v2 = Vector2d.from_string("4.2 2.5")
print(v2)  # output: (4.2, 2.5)
