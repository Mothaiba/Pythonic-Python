import copy

# == shallow and deep copy ==

l1 = [1, [2, 3], (4, 5)]
l2 = l1  # shallow copy
l3 = list(l1)  # shallow copy
l4 = copy.deepcopy(l1)  # deep copy
l1[1].append(40)

print(l1)  # output: [1, [2, 3, 40], (4, 5)]
print(l2)  # output: [1, [2, 3, 40], (4, 5)]
print(l3)  # output: [1, [2, 3, 40], (4, 5)]
print(l4)  # output: [1, [2, 3], (4, 5)]


# == Mutable object as default ==


class HauntedBus:
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = HauntedBus()
bus1.pick("Tung")
bus2 = HauntedBus()
print(bus2.passengers)  # output: ['Tung']


# == Mutable object as a parameter ==


class TwilightBus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


basketball_team = ["A", "B", "C", "D"]
bus = TwilightBus(basketball_team)
bus.drop("C")
print(basketball_team)  # output: ['A', 'B', 'D']
