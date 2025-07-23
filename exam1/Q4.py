class Time:
    def __init__(self,h=0, m=0):
        if h < 0 or h > 23:
            self._hour = 0
        else:
            self._hour = h

        if m < 0 or m > 59:
            self._minute = 0
        else:
            self._minute = m

    def get_hour(self):
        return self._hour
    def get_minute(self):
        return self._minute

    def __str__(self):
        return f"{self._hour:02d}:{self._minute:02d}"

class Date:
    def __init__(self, d, m ,y):
        self._day = d
        self._month = m
        self._year = y

    def get_day(self):
        return self._day
    def get_month(self):
        return self._month
    def get_year(self):
        return self._year

    def __eq__(self,other):
        if not isinstance(other, Date):
            return NotImplemented
        if (other.get_day() == self.get_day() and
                other.get_month() == self.get_month() and
                other.get_year() == self.get_year()):
            return True
        else:
            return False

    def __str__(self):
        return f"{self._day:02d}/{self._month:02d}/{self._year}"

class Order:
    _order_num = 1

    def __init__(self, day, month, year, hour, minute, cost=50):
        # Create Date and Time objects internally
        self._d = Date(day, month, year)
        self._t = Time(hour, minute)

        self._cost = cost

        self._order_id = Order._order_num
        Order._order_num += 1

    def get_cost(self):
        return self._cost
    def get_order_id(self):
        return self._order_id
    def get_d(self):
        return self._d
    def get_t(self):
        return self._t

    def __gt__(self,other):
        if not isinstance(other,Order):
            raise TypeError("other must be an instance of Order clas")
        if self._cost > other._cost:
            return True
        else:
            return False

    def __str__(self):
        return (f"Order ID: {self._order_id}, Date: {self._d.get_day()}/{self._d.get_month()}/{self._d.get_year()}, "
                f"Time: {self._t.get_hour()}:{self._t.get_minute()}:, Cost: {self._cost}")



class OnlineOrder(Order):
    def __init__(self, day, month, year, hour, minute, cost, username):
        super().__init__(day, month, year, hour, minute, cost)
        self._username = username


class CashRegister:
    def __init__(self):
        self._orders = []

    def monthly_total_income(self, month):
        total = 0
        for order in self._orders:
            if order.get_month() == month:
                total =+ order.get_cost()

        return total

    def most_expensive_order(self,date):
        most_expensive = 0
        for order in self._orders:
            if not order.get_d().eq(date):
                continue
            else:
                if most_expensive < order.get_cost():
                    most_expensive = order.get_cost()

        if most_expensive == 0:
            return None
        return most_expensive

    def less_than(self,cost):
        less_than = []
        for order in self._orders:
            if order.get_cost() < cost:
                less_than.append(order)

        if not less_than:
            return None
        return less_than



# Assuming the corrected classes (Time, Date, Order, OnlineOrder, CashRegister)
# are defined above or imported.

print("--- Starting Test Suite ---")

# Reset order_num for consistent testing
Order._order_num = 1

# --- Test Time Class ---
print("\n--- Testing Time Class ---")
t1 = Time(10, 30)
assert t1.get_hour() == 10, f"Time Test Failed: Expected hour 10, got {t1.get_hour()}"
assert t1.get_minute() == 30, f"Time Test Failed: Expected minute 30, got {t1.get_minute()}"
assert str(t1) == "10:30", f"Time Test Failed: Expected '10:30', got '{str(t1)}'"

t2 = Time(25, 65) # Invalid values
assert t2.get_hour() == 0, f"Time Test Failed: Expected hour 0 for invalid input, got {t2.get_hour()}"
assert t2.get_minute() == 0, f"Time Test Failed: Expected minute 0 for invalid input, got {t2.get_minute()}"
assert str(t2) == "00:00", f"Time Test Failed: Expected '00:00', got '{str(t2)}'"

t3 = Time() # Default values
assert t3.get_hour() == 0 and t3.get_minute() == 0, "Time Test Failed: Default constructor failed"
print("Time Class Tests Passed!")


# --- Test Date Class ---
print("\n--- Testing Date Class ---")
d1 = Date(15, 7, 2025)
assert d1.get_day() == 15, f"Date Test Failed: Expected day 15, got {d1.get_day()}"
assert d1.get_month() == 7, f"Date Test Failed: Expected month 7, got {d1.get_month()}"
assert d1.get_year() == 2025, f"Date Test Failed: Expected year 2025, got {d1.get_year()}"
assert str(d1) == "15/07/2025", f"Date Test Failed: Expected '15/07/2025', got '{str(d1)}'"

d2 = Date(15, 7, 2025)
d3 = Date(16, 7, 2025)

# Test __eq__
assert (d1 == d2) is True, "Date __eq__ Test Failed: Identical dates should be True"
assert (d1 == d3) is False, "Date __eq__ Test Failed: Different dates should be False"
print("Date Class Tests Passed!")


# --- Test Order Class ---
print("\n--- Testing Order Class ---")
# Test with default cost
o1 = Order(1, 1, 2024, 9, 0)
assert o1.get_cost() == 50, f"Order Test Failed: Expected default cost 50, got {o1.get_cost()}"
assert o1.get_order_id() == 1, f"Order Test Failed: Expected order ID 1, got {o1.get_order_id()}"
assert isinstance(o1.get_d(), Date), "Order Test Failed: Date object not created"
assert isinstance(o1.get_t(), Time), "Order Test Failed: Time object not created"
print(f"Order 1: {o1}")

# Test with specified cost
o2 = Order(2, 1, 2024, 10, 30, 120)
assert o2.get_cost() == 120, f"Order Test Failed: Expected cost 120, got {o2.get_cost()}"
assert o2.get_order_id() == 2, f"Order Test Failed: Expected order ID 2, got {o2.get_order_id()}"
print(f"Order 2: {o2}")

# Test __gt__
assert (o2 > o1) is True, "Order __gt__ Test Failed: o2 should be greater than o1"
assert (o1 > o2) is False, "Order __gt__ Test Failed: o1 should not be greater than o2"
o3 = Order(3, 1, 2024, 11, 0, 50)
assert (o1 > o3) is False, "Order __gt__ Test Failed: o1 should not be greater than o3 (equal cost)"

try:
    o1 > "not an order"
    assert False, "Order __gt__ Test Failed: TypeError not raised for non-Order comparison"
except TypeError as e:
    assert str(e) == "other must be an instance of Order class", "Order __gt__ Test Failed: Incorrect TypeError message"

print("Order Class Tests Passed!")


# --- Test OnlineOrder Class ---
print("\n--- Testing OnlineOrder Class ---")
oo1 = OnlineOrder(10, 2, 2024, 14, 15, 75, "john_doe")
assert oo1.get_cost() == 75, f"OnlineOrder Test Failed: Expected cost 75, got {oo1.get_cost()}"
assert oo1.get_order_id() == 3, f"OnlineOrder Test Failed: Expected order ID 3, got {oo1.get_order_id()}"
assert oo1.get_username() == "john_doe", f"OnlineOrder Test Failed: Expected username 'john_doe', got {oo1.get_username()}"
assert isinstance(oo1, Order), "OnlineOrder Test Failed: oo1 should be an instance of Order"
print(f"Online Order 1: {oo1}")
print("OnlineOrder Class Tests Passed!")


# --- Test CashRegister Class ---
print("\n--- Testing CashRegister Class ---")
cr = CashRegister()

# Test add_order
cr.add_order(o1)
cr.add_order(o2)
cr.add_order(oo1)
# Create more orders for comprehensive testing
o4 = Order(15, 7, 2025, 12, 0, 100) # July 2025
o5 = OnlineOrder(15, 7, 2025, 13, 0, 200, "jane_doe") # July 2025, most expensive online
o6 = Order(1, 1, 2024, 10, 0, 30) # Jan 2024, cost 30
o7 = OnlineOrder(15, 7, 2025, 14, 0, 180, "bob_smith") # July 2025, online, less expensive than jane_doe
o8 = Order(1, 8, 2024, 9, 0, 60) # August 2024

cr.add_order(o4)
cr.add_order(o5)
cr.add_order(o6)
cr.add_order(o7)
cr.add_order(o8)

assert len(cr._orders) == 8, f"CashRegister Test Failed: Expected 8 orders, got {len(cr._orders)}"
try:
    cr.add_order("not an order")
    assert False, "CashRegister Test Failed: TypeError not raised for non-Order object"
except TypeError as e:
    assert str(e) == "Only Order or OnlineOrder instances can be added to the cash register.", "CashRegister Test Failed: Incorrect TypeError message"
print("CashRegister add_order Tests Passed!")


# Test monthly_total_income
# Orders in Jan 2024: o1 (50), o2 (120), o6 (30) -> Total: 200
income_jan = cr.monthly_total_income(1)
assert income_jan == 200, f"CashRegister Test Failed: Monthly income for Jan 2024 expected 200, got {income_jan}"

# Orders in Feb 2024: oo1 (75) -> Total: 75
income_feb = cr.monthly_total_income(2)
assert income_feb == 75, f"CashRegister Test Failed: Monthly income for Feb 2024 expected 75, got {income_feb}"

# Orders in July 2025: o4 (100), o5 (200), o7 (180) -> Total: 480
income_jul = cr.monthly_total_income(7)
assert income_jul == 480, f"CashRegister Test Failed: Monthly income for Jul 2025 expected 480, got {income_jul}"

# No orders in month 3 (March)
income_mar = cr.monthly_total_income(3)
assert income_mar == 0, f"CashRegister Test Failed: Monthly income for Mar expected 0, got {income_mar}"
print("CashRegister monthly_total_income Tests Passed!")


# Test most_expensive_order
target_date = Date(15, 7, 2025)
# Online orders on 15/07/2025: o5 (cost 200, ID 5), o7 (cost 180, ID 7)
# Most expensive should be o5 with ID 5
most_expensive_id = cr.most_expensive_order(target_date)
assert most_expensive_id == 5, f"CashRegister Test Failed: Most expensive order ID expected 5, got {most_expensive_id}"

# Test with a date that has no online orders
no_online_date = Date(1, 1, 2024)
no_expensive_id = cr.most_expensive_order(no_online_date)
assert no_expensive_id is None, f"CashRegister Test Failed: Expected None for no online orders on date, got {no_expensive_id}"

# Test with a date that has no orders at all
empty_date = Date(1, 1, 2000)
empty_expensive_id = cr.most_expensive_order(empty_date)
assert empty_expensive_id is None, f"CashRegister Test Failed: Expected None for no orders at all, got {empty_expensive_id}"
print("CashRegister most_expensive_order Tests Passed!")


# Test less_than
# Orders with cost < 60: o1 (50), oo1 (75 - NO), o6 (30) -> Expected: [o1, o6]
less_than_60 = cr.less_than(60)
assert len(less_than_60) == 2, f"CashRegister Test Failed: Expected 2 orders less than 60, got {len(less_than_60)}"
assert o1 in less_than_60 and o6 in less_than_60, "CashRegister Test Failed: Incorrect orders in less_than_60"

# Orders with cost < 20: None
less_than_20 = cr.less_than(20)
assert less_than_20 is None, f"CashRegister Test Failed: Expected None for no orders less than 20, got {less_than_20}"

# Orders with cost < 250: All orders except o5 (200) and o7 (180) are less than 250
# o1(50), o2(120), oo1(75), o4(100), o6(30), o8(60)
less_than_250 = cr.less_than(250)
assert len(less_than_250) == 6, f"CashRegister Test Failed: Expected 6 orders less than 250, got {len(less_than_250)}"
print("CashRegister less_than Tests Passed!")

print("\n--- All Tests Completed Successfully! ---")
