from Person import Person
import message
import re


class Seller(Person):
    def __init__(self, name, surname, city, money):
        super().__init__(name, surname, city, money)
        self.car_park = []
        self.sold_cars = []

    def sell(self, car, price, store):
        if car in self.car_park:
            store.add_car(self, car, price)
        else:
            print(message.car_error)

    def add_park(self, car):
        self.car_park.append(car)

    def remove_park(self, car):
        self.car_park.remove(car)

    def add_sold(self, car):
        self.sold_cars.append(car)

    def remove_sold(self, car):
        self.sold_cars.remove(car)

    def get_cars(self, car_list):
        for car in car_list:
            print(f"---------------{car.__dict__["_make"]} {car.__dict__["_model"]}---------------")
            for atr in car.__dict__:
                if not re.match(rf"^_{car.__class__.__name__}", atr):
                    print(re.sub(r"^_", "", atr), " -> ", car.__dict__[atr])
        print("----------------------------------------")

    def get_park_cars(self):
        self.get_cars(self.car_park)

    def get_sold_cars(self):
        self.get_cars(self.sold_cars)

    def return_car(self, reason, car, store, buyer):
        if car in self.sold_cars:
            while True:
                ans = input(message.agree)
                if ans == "yes" or ans == "no":
                    store.ans_back(reason, ans, car, buyer, self)
                    break
                else:
                    print(message.yes_no)

    def check_discount(self, store):
        store.get_car_avaliable_discount(self)
