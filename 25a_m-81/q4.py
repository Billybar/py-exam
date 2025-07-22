# solved by AI

# section A
class Contract:
    pass

class Vehicle:
    pass

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

# section B
def __init__(self, name="Someone", days=1, kilos=100):
    self._name = name
    self._days = days
    self._kilos = kilos

class Vehicle:
    def __init__(self, name, days, kilos, id):
        # Call the Contract constructor to create the contract object
        self._contract = Contract(name, days, kilos)
        self._id = id

# section C
class Motorcycle(Vehicle):
    def __init__(self, name, days, kilos, id):
        super().__init__(name, days, kilos, id)
        self._off_road = False

# section D
class Vehicle:
    def __init__(self, name, days, kilos, id):
        self._contract = Contract(name, days, kilos)
        self._id = id

    def payment(self):
        price_day = 60
        price_kilo = 2
        # Access _days and _kilos from the _contract object
        total_price = price_day * self._contract._days + price_kilo * self._contract._kilos
        return total_price

class Car(Vehicle):
    def __init__(self, name, days, kilos, id, seats):
        super().__init__(name, days, kilos, id)
        self._seats = seats

    def payment(self):
        # Car payment is the same as the base Vehicle payment
        return super().payment()

class Truck(Vehicle):
    def __init__(self, name, days, kilos, id, max_weight):
        super().__init__(name, days, kilos, id)
        self._max_weight = max_weight

    def payment(self):
        basic_pay = super().payment()
        truck_fee = 500
        total_pay = basic_pay + truck_fee
        return total_pay

class Motorcycle(Vehicle):
    def __init__(self, name, days, kilos, id, off_road):
        super().__init__(name, days, kilos, id)
        self._off_road = off_road

    def payment(self):
        # Motorcycle payment is half of the base rate.
        # It needs to recalculate based on half rates, not half of super().payment()
        # because super().payment() might already include other fees not applicable to motorcycle.
        price_day = 30  # Half of 60
        price_kilo = 1  # Half of 2
        total_price = price_day * self._contract._days + price_kilo * self._contract._kilos
        return total_price

# section E
def print_payment(lst):
    for val in lst:
        print(val.payment())