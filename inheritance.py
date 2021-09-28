class DoppleDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


dd = DoppleDict(one=1)  # execute the old way
print("dd:", dd)  # output: dd: {'one': 1}
dd["two"] = 2  # execute the new way
dd.update(three=3)  # execute the old way
print("dd:", dd)  # output: dd: {'one': 1, 'two': [2, 2], 'three': 3}
