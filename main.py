from CarMarket import CarMarket
from car import Car
from Seller import Seller
from Buyer import Buyer
kia_optima = Car(
    vin="1HGCM82633A123456",
    make="KIA",
    model="Optima",
    year=2017,
    trim="FE",
    color="Black",
    engine="2.4 GDI",
    horse_power=185,
    fuel_type="Gasoline",
    drivetrain="FWD",
    interior_color="Black",
    wheels=16)
toyota_camry = Car(
    vin="4T1BE46K07U123456",
    year=2020,
    make="Toyota",
    model="Camry",
    trim="LE",
    color="Silver",
    engine="2.5L I4",
    horse_power=203,
    fuel_type="Gasoline",
    drivetrain="FWD",
    interior_color="Gray",
    wheels=17
)
xanut = CarMarket("cars.json","sold_cars.json")
noro = Seller(name="Norayr", surname="Hovhannisyan", city="Yerevan", money=0)
fof = Seller(name="Fof", surname="Manukyan", city="Yerevan", money=0)
tyom = Seller(name="tyom", surname="vardanyan", city="Yerevan", money=0)
jorj = Buyer(name="Seroj", surname="Husyan", city="Yerevan", money=29000)

noro.add_park(kia_optima)
noro.sell(kia_optima, 12000, xanut)
xanut._set_discount(kia_optima, 3000)
tyom.check_discount()
