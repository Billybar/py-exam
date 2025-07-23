class Date:
    def __init__(self, d, m, y):
        self.day_ = d
        self.month_ = m
        self.year_ = y

    def get_day(self):
        return self.day_

    def get_month(self):
        return self.month_

    def get_year(self):
        return self.year_

    def __eq__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        return (self.day_ == other.day_ and
                self.month_ == other.month_ and
                self.year_ == other.year_)

    # Section 4.a
    def __lt__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        if self.year_ < other.year_:
            return True
        if self.year_ == other.year_:
            if self.month_ < other.month_:
                return True
            if self.month_ == other.month_:
                return self.day_ < other.day_
        return False

    def __str__(self):
        return f"{self.day_}/{self.month_}/{self.year_}"


class Person:
    # Section 4.b
    def __init__(self, name, id, birth):
        self.name_ = name
        self.id_ = id
        self.birth_ = birth

    def get_name(self):
        return self.name_

    def get_id(self):
        return self.id_

    def get_birth(self):
        return self.birth_

    # Section 4.c
    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name_ == other.name_ and self.birth_ == other.birth_

    def __str__(self):
        return f"Name: {self.name_}, ID: {self.id_}, Birth Date: {self.birth_}"


class Friend(Person):
    # Section 4.d
    def __init__(self, name, id, birth, closeness=0):
        super().__init__(name, id, birth)
        self.closeness_ = closeness

    def get_closeness(self):
        return self.closeness_

    # Section 4.e
    def __eq__(self, other):
        if not isinstance(other, Friend):
            return NotImplemented
        # Reuse Person's __eq__ for name and birth date comparison
        return super().__eq__(other) and self.closeness_ == other.closeness_

    def __str__(self):
        return f"Name: {self.name_}, ID: {self.id_}, Birth Date: {self.birth_}, Closeness: {self.closeness_}"


class ContactsList:
    def __init__(self):
        self.contacts_ = []

    def add_contact(self, contact):
        self.contacts_.append(contact)

    # Section 4.f
    def born_in_date(self, date):
        count = 0
        # Iterate through contacts to find Friends with closeness 3 (work friends)
        # and check if their birth date matches the given date.
        for contact in self.contacts_:
            if isinstance(contact, Friend) and contact.get_closeness() == 3:
                if contact.get_birth() == date:
                    count += 1
        return count

    # Section 4.g
    def oldest_contact(self):
        if not self.contacts_:
            return None

        oldest = None
        # Iterate through contacts to find the one with the earliest birth date.
        for contact in self.contacts_:
            if oldest is None or contact.get_birth() < oldest.get_birth():
                oldest = contact
        return oldest.get_name() if oldest else None


    # Section 4.h
    def born_in_month(self):
        if not self.contacts_:
            return None

        # Dictionary to store birth counts for each month.
        month_counts = {}
        for contact in self.contacts_:
            month = contact.get_birth().get_month()
            month_counts[month] = month_counts.get(month, 0) + 1

        # Convert the dictionary to a list of tuples without using short syntax
        result = []
        for month, count in month_counts.items():
            result.append((month, count))

        # Sort the list of tuples by month number
        result.sort()  # By default, sort will use the first element of the tuple

        return result


import unittest

# Assume the classes Date, Person, Friend, ContactsList are defined in a file named 'contacts_management.py'
# For the purpose of this example, I'll include them directly here.
# In a real scenario, you would do:
# from contacts_management import Date, Person, Friend, ContactsList

class Date:
    def __init__(self, d, m, y):
        self.day_ = d
        self.month_ = m
        self.year_ = y

    def get_day(self):
        return self.day_

    def get_month(self):
        return self.month_

    def get_year(self):
        return self.year_

    def __eq__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        return (self.day_ == other.day_ and
                self.month_ == other.month_ and
                self.year_ == other.year_)

    def __lt__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        if self.year_ < other.year_:
            return True
        if self.year_ == other.year_:
            if self.month_ < other.month_:
                return True
            if self.month_ == other.month_:
                return self.day_ < other.day_
        return False

    def __str__(self):
        return f"{self.day_}/{self.month_}/{self.year_}"


class Person:
    def __init__(self, name, id, birth):
        self.name_ = name
        self.id_ = id
        self.birth_ = birth

    def get_name(self):
        return self.name_

    def get_id(self):
        return self.id_

    def get_birth(self):
        return self.birth_

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name_ == other.name_ and self.birth_ == other.birth_

    def __str__(self):
        return f"Name: {self.name_}, ID: {self.id_}, Birth Date: {self.birth_}"


class Friend(Person):
    def __init__(self, name, id, birth, closeness=0):
        super().__init__(name, id, birth)
        self.closeness_ = closeness

    def get_closeness(self):
        return self.closeness_

    def __eq__(self, other):
        if not isinstance(other, Friend):
            return NotImplemented
        return super().__eq__(other) and self.closeness_ == other.closeness_

    def __str__(self):
        return f"Name: {self.name_}, ID: {self.id_}, Birth Date: {self.birth_}, Closeness: {self.closeness_}"


class ContactsList:
    def __init__(self):
        self.contacts_ = []

    def add_contact(self, contact):
        self.contacts_.append(contact)

    def born_in_date(self, date):
        count = 0
        for contact in self.contacts_:
            if isinstance(contact, Friend) and contact.get_closeness() == 3:
                if contact.get_birth() == date:
                    count += 1
        return count

    def oldest_contact(self):
        if not self.contacts_:
            return None

        oldest = None
        for contact in self.contacts_:
            if oldest is None or contact.get_birth() < oldest.get_birth():
                oldest = contact
        return oldest.get_name() if oldest else None

    def born_in_month(self):
        if not self.contacts_:
            return None

        month_counts = {}
        for contact in self.contacts_:
            month = contact.get_birth().get_month()
            month_counts[month] = month_counts.get(month, 0) + 1

        result = []
        for month, count in month_counts.items():
            result.append((month, count))

        result.sort()

        return result


class TestDate(unittest.TestCase):
    def test_date_init(self):
        d1 = Date(15, 7, 2023)
        self.assertEqual(d1.get_day(), 15)
        self.assertEqual(d1.get_month(), 7)
        self.assertEqual(d1.get_year(), 2023)

    def test_date_equality(self):
        d1 = Date(10, 5, 2020)
        d2 = Date(10, 5, 2020)
        d3 = Date(11, 5, 2020)
        d4 = Date(10, 6, 2020)
        d5 = Date(10, 5, 2021)

        self.assertEqual(d1, d2)
        self.assertNotEqual(d1, d3)
        self.assertNotEqual(d1, d4)
        self.assertNotEqual(d1, d5)
        self.assertNotEqual(d1, "not a date")

    def test_date_less_than(self):
        d1 = Date(1, 1, 2000)
        d2 = Date(1, 1, 2001)
        d3 = Date(1, 2, 2000)
        d4 = Date(2, 1, 2000)
        d5 = Date(1, 1, 2000)

        self.assertTrue(d1 < d2)  # Different year
        self.assertTrue(d1 < d3)  # Same year, different month
        self.assertTrue(d1 < d4)  # Same year, same month, different day
        self.assertFalse(d2 < d1)
        self.assertFalse(d5 < d1) # Not strictly less than
        self.assertFalse(d1 < d5) # Not strictly less than
        self.assertFalse(d1 < Date(31, 12, 1999)) # Not less than


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.d1 = Date(1, 1, 1990)
        self.d2 = Date(2, 2, 1991)
        self.p1 = Person("Alice", "123", self.d1)
        self.p2 = Person("Alice", "456", self.d1) # Same name, birth date, different ID
        self.p3 = Person("Bob", "123", self.d1)   # Different name
        self.p4 = Person("Alice", "123", self.d2) # Different birth date

    def test_person_init(self):
        self.assertEqual(self.p1.get_name(), "Alice")
        self.assertEqual(self.p1.get_id(), "123")
        self.assertEqual(self.p1.get_birth(), self.d1)

    def test_person_equality(self):
        self.assertEqual(self.p1, self.p2) # Equal due to name and birth date
        self.assertNotEqual(self.p1, self.p3)
        self.assertNotEqual(self.p1, self.p4)
        self.assertNotEqual(self.p1, "not a person")


class TestFriend(unittest.TestCase):
    def setUp(self):
        self.d1 = Date(1, 1, 1990)
        self.d2 = Date(2, 2, 1991)
        self.f1 = Friend("Charlie", "789", self.d1, 1)
        self.f2 = Friend("Charlie", "012", self.d1, 1) # Same name, birth date, closeness, different ID
        self.f3 = Friend("Charlie", "789", self.d1, 2) # Different closeness
        self.f4 = Friend("David", "789", self.d1, 1)   # Different name
        self.f5 = Friend("Charlie", "789", self.d2, 1) # Different birth date
        self.f6 = Friend("Eve", "345", Date(5, 5, 1985)) # For default closeness test
        self.person = Person("Charlie", "789", self.d1) # A person, not a friend

    def test_friend_init(self):
        self.assertEqual(self.f1.get_name(), "Charlie")
        self.assertEqual(self.f1.get_id(), "789")
        self.assertEqual(self.f1.get_birth(), self.d1)
        self.assertEqual(self.f1.get_closeness(), 1)
        self.assertEqual(self.f6.get_closeness(), 0) # Test default closeness

    def test_friend_equality(self):
        self.assertEqual(self.f1, self.f2) # Equal due to name, birth date, closeness
        self.assertNotEqual(self.f1, self.f3)
        self.assertNotEqual(self.f1, self.f4)
        self.assertNotEqual(self.f1, self.f5)
        self.assertNotEqual(self.f1, self.person) # Not equal to a Person object


class TestContactsList(unittest.TestCase):
    def setUp(self):
        self.contacts_list = ContactsList()

        self.d_alice = Date(10, 5, 1985)
        self.d_bob = Date(15, 5, 1990)
        self.d_charlie = Date(20, 6, 1985)
        self.d_diana = Date(10, 5, 1985) # Same birth date as Alice
        self.d_eve = Date(1, 1, 1980)  # Oldest

        self.p_alice = Person("Alice", "P001", self.d_alice)
        self.f_bob_work = Friend("Bob", "F001", self.d_bob, 3) # Work friend
        self.f_charlie_close = Friend("Charlie", "F002", self.d_charlie, 1) # Close friend
        self.f_diana_work = Friend("Diana", "F003", self.d_diana, 3) # Work friend, same birth date as Alice
        self.f_eve_distant = Friend("Eve", "F004", self.d_eve, 2) # Distant friend, oldest

        self.contacts_list.add_contact(self.p_alice)
        self.contacts_list.add_contact(self.f_bob_work)
        self.contacts_list.add_contact(self.f_charlie_close)
        self.contacts_list.add_contact(self.f_diana_work)
        self.contacts_list.add_contact(self.f_eve_distant)

    def test_born_in_date_empty(self):
        empty_list = ContactsList()
        test_date = Date(1, 1, 2000)
        self.assertEqual(empty_list.born_in_date(test_date), 0)

    def test_born_in_date_with_matches(self):
        # Alice (Person) - not a Friend
        # Bob (Work friend, May 15)
        # Charlie (Close friend, June 20)
        # Diana (Work friend, May 10)
        # Eve (Distant friend, Jan 1)

        # Work friends born on May 10, 1985: Diana
        self.assertEqual(self.contacts_list.born_in_date(Date(10, 5, 1985)), 1)
        # Work friends born on May 15, 1990: Bob
        self.assertEqual(self.contacts_list.born_in_date(Date(15, 5, 1990)), 1)

    def test_born_in_date_no_matches(self):
        # No work friends born on April 1, 2000
        self.assertEqual(self.contacts_list.born_in_date(Date(1, 4, 2000)), 0)
        # Bob is a work friend but born on a different date
        self.assertEqual(self.contacts_list.born_in_date(Date(1, 1, 1990)), 0)

    def test_oldest_contact_empty(self):
        empty_list = ContactsList()
        self.assertIsNone(empty_list.oldest_contact())

    def test_oldest_contact_single(self):
        single_contact_list = ContactsList()
        single_contact_list.add_contact(self.p_alice)
        self.assertEqual(single_contact_list.oldest_contact(), "Alice")

    def test_oldest_contact_multiple(self):
        # Eve (Jan 1, 1980) is the oldest
        self.assertEqual(self.contacts_list.oldest_contact(), "Eve")

    def test_oldest_contact_same_birth_date(self):
        # Add another contact with the same birth date as the current oldest
        # The problem states "Assumed there is a single contact that meets the condition"
        # So this specific scenario is not strictly required to be tested according to the prompt
        # But if it were, the first encountered "oldest" would be returned.
        d_eve_clone = Date(1, 1, 1980)
        f_eve_clone = Friend("Eve Clone", "F005", d_eve_clone, 1)
        self.contacts_list.add_contact(f_eve_clone)
        # Depending on insertion order, either "Eve" or "Eve Clone" could be returned.
        # Since the problem assumes a single oldest, this test focuses on a clear oldest.
        # If order matters for ties, `min()` with a key or a custom sort would be needed.
        self.assertEqual(self.contacts_list.oldest_contact(), "Eve") # Eve was added first

    def test_born_in_month_empty(self):
        empty_list = ContactsList()
        self.assertIsNone(empty_list.born_in_month())

    def test_born_in_month_multiple_months(self):
        # Alice (May), Bob (May), Charlie (June), Diana (May), Eve (Jan)
        expected = [(1, 1), (5, 3), (6, 1)] # Sorted by month
        self.assertEqual(self.contacts_list.born_in_month(), expected)

    def test_born_in_month_no_contacts_for_some_months(self):
        # If there were contacts but none in a specific month (e.g., month 2), it should not appear.
        # Our existing setup already implicitly tests this, as no one is born in February, March, etc.
        expected = [(1, 1), (5, 3), (6, 1)]
        self.assertEqual(self.contacts_list.born_in_month(), expected)

    def test_born_in_month_single_month(self):
        single_month_list = ContactsList()
        single_month_list.add_contact(Person("A", "1", Date(1, 3, 2000)))
        single_month_list.add_contact(Person("B", "2", Date(5, 3, 1990)))
        expected = [(3, 2)]
        self.assertEqual(single_month_list.born_in_month(), expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)