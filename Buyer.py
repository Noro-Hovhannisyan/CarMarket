from Person import Person
import message
import re


class Buyer(Person):
    def __init__(self, name, surname, city, money):
        super().__init__(name, surname, city, money)
        self.bought_cars = []
        self.spent_money = 0

    def buy(self,car,store):
        store.sell_car(self, car)

    def return_car(self, reason, car, store):
        if car in self.bought_cars:
            store.return_car(reason, car, self)
        else:
            print(message.car_error)

    def print_my_cars(self):
        for car in self.bought_cars:
            print(f"---------------{car.__dict__["_make"]} {car.__dict__["_model"]}---------------")
            for atr in car.__dict__:
                if not re.match(rf"^_{car.__class__.__name__}", atr):
                    print(re.sub(r"^_", "", atr), " -> ", car.__dict__[atr])
        print("----------------------------------------")

