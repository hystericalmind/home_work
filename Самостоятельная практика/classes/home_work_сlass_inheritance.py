class Car:
    price = 1000000

    def horse_powers(self, hp):
        self.hp = hp
        print(f'HP = {hp}')
class Nissan(Car):
    pass
    price = 2000000

    def horse_powers(self, hp):
        print(f'This is Nissan, price = {self.price}, my HP = {hp}')


class Kia(Car):
    price = 900000
    def horse_powers(self, hp):
        print(f'This is KIA, price = {self.price} my HP = {hp}')




car = Car()
nissan = Nissan()
kia = Kia()

car.horse_powers(149)
nissan.horse_powers(200)
kia.horse_powers(115)