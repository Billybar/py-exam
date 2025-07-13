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
        if other.get_day == self.get_day and other.get_month == self.get_month and other.get_year == self.get_year:
            return True
        else:
            return False


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
    def order_id(self):
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


