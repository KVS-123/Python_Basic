
class Property:
    def __init__(self, worth):
        self.worth = worth

    def tax_calculation(self):
        return self.worth / 20


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth / 500


money = int(input('Сколько у вас денег? '))

apartament = Apartment(int(input('\nСколько стоит квартира? ')))
car = Car(int(input('Сколько стоит машина? ')))
house = CountryHouse(int(input('Сколько стоит дом? ')))

tax = apartament.tax_calculation() + car.tax_calculation() + house.tax_calculation()
if money < tax:
    print('Вам не хватает', tax - money)
else:
    print('Вам хватает денег для оплаты налога')
