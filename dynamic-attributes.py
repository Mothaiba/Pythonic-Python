class C:
    pass


obj = C()
obj.attr_1 = "1st attribute"

obj.__dict__.update(
    {"attr_2": "2nd attribute", "attr_3": 3,}
)

print(obj.__dict__)
print(obj.attr_3)
