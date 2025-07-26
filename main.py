from rental import Car
from user import User

c1 = Car("Toyota", "Corolla", "C001", 2000)
u1 = User("Ahmad", 17, 3)
c1.display()
u1.rent_car(c1)
