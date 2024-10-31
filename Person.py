import message


class Person:
    def __init__(self, name, surname, city, money=0):
        self.name = name
        self.surname = surname
        self.city = city
        self.money = money

    def change_money(self, action, value):
        if action == "+":
            self.money += value
        elif action == "-":
            self.money -= value
        else:
            print(message.action)
