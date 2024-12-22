class BaseDish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_details(self):
        print(f"{self.name}: {self.price} грн")

class Drink:
    def __init__(self, name, price, volume):
        self.name = name
        self.price = price
        self.volume = volume

    def show_details(self):
        print(f"{self.name}: {self.price} грн, {self.volume}")

class ComboMeal:
    def __init__(self, dish_name, dish_price, drink_name, drink_price, drink_volume, discount):
        self.dish_name = dish_name
        self.dish_price = dish_price
        self.drink_name = drink_name
        self.drink_price = drink_price
        self.drink_volume = drink_volume
        self.discount = discount

    def show_details(self):
        print(f"{self.dish_name} + {self.drink_name}: {self.dish_price + self.drink_price - self.discount} грн зі знижкою {self.discount} грн")


burger = BaseDish("Бургер", 80)
cola = Drink("Кола", 25, "500 мл")
combo = ComboMeal("Бургер", 80, "Кола", 25, "500 мл", 15)


burger.show_details()
cola.show_details()
combo.show_details()
