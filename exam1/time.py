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

class Order:


