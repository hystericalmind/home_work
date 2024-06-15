class Vihicle:
    vehicle_type = None
    def __init__(self,vehicle_type):
        self.price = vehicle_type

class Car:
    price = 1000000
    def __init__(self,price):
        self.price = price
    def horse_powers(self, hp):
        self.hp = hp
        return  hp

class Nissan(Car, Vihicle):
    def __init__(self, vehicle_type, price):
        super().__init__(vehicle_type)
        super().__init__(price)
        super().horse_powers(150)

nissan = Nissan(True, 90000000)
print(nissan.vehicle_type, nissan.price)
