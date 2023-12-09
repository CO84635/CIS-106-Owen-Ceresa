class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price
        self.discount_price = 0.9 * sticker_price

    def price_w_options(self):
        return f"Make: {self.make}, Model: {self.model}, Sticker Price: {self.sticker_price}"

class Sports(Car):
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price
        self.discount_price = 0.9 * sticker_price
        self.sports_wheels_option = False
        self.sports_engine_option = False
        self.sports_interior_option = False

    def add_sports_wheels(self):
        self.sports_wheels_option = True
        self.discount_price += 1000.00

    def add_sports_engine(self):
        self.sports_engine_option = True
        self.discount_price += 3000.00

    def add_sports_interior(self):
        self.sports_interior_option = True
        self.discount_price += 2000.00

    def pricewithoptions(self):
        options_str = ""
        if self.sports_wheels_option:
            options_str += "SportWheels, "
        if self.sports_engine_option:
            options_str += "SportEngine, "
        if self.sports_interior_option:
            options_str += "SportInterior, "

        if options_str:
            options_str = options_str[:-2]

        return f"Make: {self.make}, Model: {self.model}, Price with Options {options_str}: ${self.discount_price}"

car_1 = Sports('Pontiac', 'Grand Prix', 20000)
car_1.add_sports_wheels()
car_1.add_sports_engine()

car_2 = Sports('Chrysler', 'Town and Country', 22000)
car_2.add_sports_wheels()
car_2.add_sports_engine()
car_2.add_sports_interior()

print(car_1.pricewithoptions())
print(car_2.pricewithoptions())
