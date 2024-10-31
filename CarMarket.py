import manager
import re
import message
from datetime import datetime

manager = manager.JsonManager()


class CarMarket:
    def __init__(self, cars, history):
        self.cars = cars
        self.history = history
        self.sellers = []

    @property
    def cars(self):
        return self._cars

    @cars.setter
    def cars(self, value):
        if isinstance(value, str) and re.search(r"\.json$", value):
            self._cars = value
        else:
            raise TypeError(message.json)

    @property
    def history(self):
        return self._history

    @history.setter
    def history(self, value):
        if isinstance(value, str) and re.search(r"\.json$", value):
            self._history = value
        else:
            raise TypeError(message.json)

    def add_car(self, caller, car, price):
        if not caller in self.sellers:
            self.sellers.append(caller)
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        data = self.stock()
        data[car.vin] = {
            "action_info": {
                "seller": {"id": id(caller), "name": caller.name, "surname": caller.surname, "city": caller.city,
                           "sell_date": date, "price": price},
            },
            "car_info": {},
        }

        for atr in car.__dict__:
            if not re.match(rf"^_{car.__class__.__name__}", atr):
                data[car.vin]["car_info"][re.sub(r"^_", "", atr)] = car.__dict__[atr]
        manager.dump(data, self.cars)

    def __remove_car(self, car):
        data = self.stock()
        del data[car.vin]
        manager.dump(data, self.cars)

    def _set_discount(self, car, value):
        data = self.stock()
        if car.vin in data:
            data[car.vin]["action_info"]["seller"]["discount"] = value
            data[car.vin]["action_info"]["seller"]["price"] -= value
        else:
            print(message.car_error)
        manager.dump(data, self.cars)

    def stock(self):
        data = manager.load(self.cars)
        return data

    def get_sold_car_history(self):
        data = manager.load(self.history)
        return data

    def add_sold_car_history(self, caller, car):
        data = manager.load(self.history)
        data[car.vin] = self.stock()[car.vin]
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        data[car.vin]["action_info"]["buyer"] = {"name": caller.name, "surname": caller.surname, "city": caller.city,
                                                 "buy_date": date}
        manager.dump(data, self.history)

    def sell_car(self, caller, car):
        if car.vin in self.stock():
            if caller.money >= self.stock()[car.vin]["action_info"]["seller"]["price"]:
                caller.money -= self.stock()[car.vin]["action_info"]["seller"]["price"]
                caller.spent_money += self.stock()[car.vin]["action_info"]["seller"]["price"]
                caller.bought_cars.append(car)
                for person in self.sellers:
                    if id(person) == self.stock()[car.vin]["action_info"]["seller"]["id"]:
                        person.money += self.stock()[car.vin]["action_info"]["seller"]["price"]
                        person.remove_park(car)
                        person.add_sold(car)
                self.add_sold_car_history(caller, car)
                self.__remove_car(car)
            else:
                print(message.money)
        else:
            print(message.car_error)

    def return_car(self, reason, car, buyer):
        if car.vin in self.get_sold_car_history():
            for person in self.sellers:
                if id(person) == self.get_sold_car_history()[car.vin]["action_info"]["seller"]["id"]:
                    person.return_car(reason, car, self, buyer)
                else:
                    print(message.car_error)

    def ans_back(self, reason, ans, car, buyer, seller):
        if ans == "yes":
            car.returned = True
            car.returned_reason = reason
            buyer.bought_cars.remove(car)
            buyer.change_money("+", self.get_sold_car_history()[car.vin]["action_info"]["seller"]["price"])
            seller.remove_sold(car)
            seller.add_park(car)
            seller.change_money("-", self.get_sold_car_history()[car.vin]["action_info"]["seller"]["price"])
            data = self.get_sold_car_history()
            del data[car.vin]
            manager.dump(data, self.history)

        else:
            print(message.no)

    def get_seller_available_cars(self, seller):
        if seller in self.sellers:
            for car in self.stock():
                if id(seller) == self.stock()[car]["action_info"]["seller"]["id"]:
                    print(f"{self.stock()[car]["car_info"]["make"]} {self.stock()[car]["car_info"]["model"]}")

    def get_car_avaliable_discount(self, seller=None):
        if seller == None:
            for car in self.stock():
                if "discount" in self.stock()[car]["action_info"]["seller"]:
                    print(
                        f"{self.stock()[car]["car_info"]["make"]} {self.stock()[car]["car_info"]["model"]} {self.stock()[car]["action_info"]["seller"]["price"]} ({self.stock()[car]["action_info"]["seller"]["discount"]})")
        else:
            if seller in self.sellers:
                for car in self.stock():
                    if id(seller) == self.stock()[car]["action_info"]["seller"]["id"]:
                        if "discount" in self.stock()[car]["action_info"]["seller"]:
                            print(
                                f"{self.stock()[car]["car_info"]["make"]} {self.stock()[car]["car_info"]["model"]} {self.stock()[car]["action_info"]["seller"]["price"]} ({self.stock()[car]["action_info"]["seller"]["discount"]})")
            else:
                print(message.seller_error)
