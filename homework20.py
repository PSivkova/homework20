#     Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
#     Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers,
#     которая возвращает количество лошидиных сил для автомобиля
#     Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type,
#     а также переопределите функцию horse_powers
#     Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price

class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000

    def horse_powers(self):
        return 200


class Nissan(Car, Vehicle):
    price = 5000000
    vehicle_type = "Skyline"

    def horse_powers(self):
        return 150


nissan = Nissan()
print(nissan.vehicle_type)
print(nissan.price)


