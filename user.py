class User:
    def __init__(self, name, age, rent_days):
        self.name = name
        self.age = age
        self.rent_days = rent_days
        self.rented_car = None  
        
    def rent_car(self, car):
        self.rented_car = car
        final = car.price * self.rent_days
        print(f"{self.name} rented {car.brand} {car.model} for {self.rent_days} days")
        print(f"Total rent = Rs {final}")
