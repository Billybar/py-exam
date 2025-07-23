# Assuming Date class is defined as per the problem description for context
class Date:
    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    # Getters for Date attributes (not explicitly asked to implement,
    # but good practice if needed)
    def get_day(self):
        return self._day

    def get_month(self):
        return self._month

    def get_year(self):
        return self._year


# Class definitions based on the problem description
# Section 5.a: Class headers
class Event:
    # Section 5.b: Constructor for Event class
    def __init__(self, hour, day, month, year):
        self._date = Date(day, month, year)
        self._hour = hour

    # Section 5.d: match function for Event (base class implementation)
    def match(self, name):
        return False

    # Getters for Event attributes (not explicitly asked to implement,
    # but good practice if needed)
    def get_date(self):
        return self._date

    def get_hour(self):
        return self._hour


class Meeting(Event):
    def __init__(self, hour, day, month, year, names, duration, location):
        super().__init__(hour, day, month, year)
        self._names = names
        self._duration = duration
        self._location = location

    # Section 5.d: match function for Meeting class
    def match(self, name):
        for mem in self._names:
            if mem == name:
                return True
        return False

    # Getters for Meeting attributes
    def get_names(self):
        return self._names

    def get_duration(self):
        return self._duration

    def get_location(self):
        return self._location


class PhoneCall(Event):
    # Section 5.c: Constructor for PhoneCall class
    def __init__(self, hour, day, month, year, phone_number, name):
        super().__init__(hour, day, month, year)
        self._phone_number = phone_number
        self._name = name

    # Section 5.d: match function for PhoneCall class
    def match(self, name):
        return self._name == name

    # Getters for PhoneCall attributes
    def get_phone_number(self):
        return self._phone_number

    def get_name(self):
        return self._name


class Task(Event):
    def __init__(self, hour, day, month, year, title):
        super().__init__(hour, day, month, year)
        self._title = title

    # Section 5.d: match function for Task class - does not explicitly
    # match by name, so returns False
    # As per problem, for other cases (like Task), it should return False.
    def match(self, name):
        return False

    # Getter for Task attribute
    def get_title(self):
        return self._title


# Section 5.e: match_events function
def match_events(events, name):
    result = []
    for event in events:
        if event.match(name):
            result.append(event)
    return result if result else None