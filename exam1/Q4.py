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
            return False
        if other.get_day == self.get_day and other.get_month == self.get_month and other.get_year == self.get_year:
            return True
        return None


class Order:
    _order_num = 1

    def __init__(self, t, d, cost=50):
        if not isinstance(t,Time):
            raise TypeError("t must be an instance of Time class")
        if not isinstance(d,Date):
            raise TypeError("d must be an instance of Date class")

        self._t = t
        self._d = d
        self._cost = cost

        self._order_id = Order._order_num
        Order._order_num += 1


    def __gt__(self,other):
        if not isinstance(other,Order):
            raise TypeError("other must be an instance of Order class")
        if self._cost > other._cost:
            return True
        else:
            return False



    def __str__(self):
        return (f"Order ID: {self._order_id}, Date: {self._d.get_day()}/{self._d.get_month()}/{self._d.get_year()}, "
                f"Time: {self._t.get_hour()}:{self._t.get_minute()}:, Cost: {self._cost}")



class OnlineOrder(Order):
    def __init__(self, t, d, cost, username):
        try:
            super().__init__(t,d,cost)
        except TypeError as e:
            raise e

        self._username = username