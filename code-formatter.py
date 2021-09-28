class Laptop:
    def __init__(self, model_name, price):
        self._model_name = model_name
        self._price = price

    def get_price(self):
        print(self._price)


laptop = Laptop("Vivobook S15", 1000)
