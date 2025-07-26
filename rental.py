class Car:
    def __init__(self, brand, model, c_id, price):
        self.brand = brand
        self.model = model
        self.c_id = c_id
        self.price = price

    def display(self):
        print(f"{self.c_id}: {self.brand} {self.model}  Rs {self.price}/day")
