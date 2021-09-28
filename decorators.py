from dataclasses import dataclass
from typing import Tuple


class Vector:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @classmethod
    def from_string(cls, s: str):
        x, y = s.split()
        return Vector(float(x), float(y))

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if isinstance(value, float):
            self._x = value
        else:
            raise ValueError("Cannot set x to a non-float.")

    def __repr__(self):
        return f"Vector({self._x}, {self._y})"


class Util:
    @staticmethod
    def load_and_parse_file(file_path: str):
        with open(file_path, "r") as f:
            content = f.read()
            lines = content.split("\n")
            return lines

    @staticmethod
    def save_files(content: str, file_path: str):
        with open(file_path, "w") as f:
            f.write(content)


@dataclass(frozen=True)  # set frozen=True to make it hashable
class Invoice:
    customer_id: int
    list_of_purchases: Tuple[float]

    def calculate_total_purchase(self):
        return sum(self.list_of_purchases)


v = Vector(1.2, 4.2)
print(v)  # output: Vector(1.2, 4.2)

w = Vector.from_string("2.5 3.2")
print(w)  # output: Vector(2.5, 3.2)

print(v.x)  # output: 1.2

try:
    v.x = "this is a string"  # output: ValueError: Cannot set x to a non-float.
except ValueError as e:
    print(e)

# this works because @dataclass handles the __init__
invoice = Invoice(123, (32.2, 11.99, 6.8))
# this works because @dataclass handle the __repr__
print(invoice)  # output: Invoice(customer_id=123, list_of_purchases=(32.2, 11.99, 6.8))
# this works because a dataclass is still a class, it can have user-defined methods
print(invoice.calculate_total_purchase())
# this works because dataclass handles __eq__ and __hash__ as we set frozen=True
print(hash(invoice))
