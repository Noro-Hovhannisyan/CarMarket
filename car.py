import message
import manager
input_manager = manager.InputManager()


class Car:
    def __init__(self, vin, year, make, model, trim, color, engine, horse_power, fuel_type, drivetrain, interior_color,
                 wheels):
        #Flags
        self.__flag_set = {"vin": True, "make": True, "model": True, "year": True}
        #Options
        self.vin = vin
        self.make = make
        self.model = model
        self.year = year
        self.trim = trim
        self.color = color
        self.engine = engine
        self.horse_power = horse_power
        self.fuel_type = fuel_type
        self.drivetrain = drivetrain
        self.interior_color = interior_color
        self.wheels = wheels
    # VIN
    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value):
        if self.__flag_set["vin"]:
            self.__flag_set["vin"] = False
            self._vin = None
            self._vin = input_manager.must_be_string(value)
        else:
            print(message.dont_change)

    # --------------------------------

    # YEAR
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if self.__flag_set["year"]:
            self.__flag_set["year"] = False
            self._year = None
            self._year = input_manager.must_be_int(value)
        else:
            print(message.dont_change)

    # --------------------------------

    # MAKE
    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        if self.__flag_set["make"]:
            self.__flag_set["make"] = False
            self._make = None
            self._make = input_manager.must_be_string(value)
        else:
            print(message.dont_change)

    # --------------------------------

    # MODEL
    @property
    def model(self):
        return self._make

    @model.setter
    def model(self, value):
        if self.__flag_set["model"]:
            self.__flag_set["model"] = False
            self._model = None
            self._model = input_manager.must_be_string(value)
        else:
            print(message.dont_change)

    # --------------------------------

    # TRIM
    @property
    def trim(self):
        return self._trim

    @trim.setter
    def trim(self, value):
        self._trim = input_manager.must_be_string(value)

    # --------------------------------

    # COLOR
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = input_manager.must_be_string(value)

    # --------------------------------

    # ENGINE
    @property
    def engine(self):
        return self.engine
    @engine.setter
    def engine(self, value):
        self._engine = value

    # --------------------------------

    # HORSE_POWER
    @property
    def horse_power(self):
        return self._horse_power

    @horse_power.setter
    def horse_power(self, value):
        self._horse_power = input_manager.must_be_int(value)

    # --------------------------------

    # FUEL_TYPE
    @property
    def fuel_type(self):
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, value):
        self._fuel_type = input_manager.must_be_string(value)

    # --------------------------------

    # DRIVETRAIN
    @property
    def drivetrain(self):
        return self._drivetrain

    @drivetrain.setter
    def drivetrain(self, value):
        self._drivetrain = input_manager.must_be_string(value)

    # --------------------------------

    # INTERIOR_COLOR
    @property
    def interior_color(self):
        return self._interior_color

    @interior_color.setter
    def interior_color(self, value):
        self._interior_color = input_manager.must_be_string(value)

    # --------------------------------

    # WHEELS
    @property
    def wheels(self):
        return self._wheels

    @wheels.setter
    def wheels(self, value):
        self._wheels = input_manager.must_be_int(value)
    # --------------------------------

