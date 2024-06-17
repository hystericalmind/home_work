class Vihicle:
    vehicle_type = None
    def __init__(self,vehicle_type):
        pass

class Car:
    price = 1000000
    def __init__(self,price):
        pass
    def horse_powers(self, hp):
        self.hp = hp
        return hp

class Nissan(Car, Vihicle):
    def __init__(self,vehicle_type, price, ):
        super().__init__(Car.horse_powers)
        super().__init__(vehicle_type)
        self.vehicle_type = 999
        super().__init__(price)
        # super().horse_powers(self.hp)
        # super().horse_powers(self.hp)

    def horse_powers(self, hp):
        super().horse_powers(hp)
        self.hp = ('переопределил получается ?')
        print(self.hp)






nissan = Nissan('ни че не меняется', 90000000)
print(nissan.horse_powers(200))
print(nissan.vehicle_type, nissan.price)
