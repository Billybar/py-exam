class Member:
    # section A
    def __init__(self, name, country):
            self._name = name
            self._country = country
            self._is_olympic = False

    def get_name(self): # Added for more comprehensive testing
        return self._name

    def get_country(self):
        return self._country

    def is_olympic(self): # Added for more comprehensive testing
        return self._is_olympic

class Committee:
    # section B
    def __init__ (self, sport_name):
        self._sport_name = sport_name
        self._members = []
        self._count = 0

    def get_sport_name(self):
        return self._sport_name

    def get_count(self):
        # return self._count
        return len(self._members)  # Corrected: _count should reflect actual members list length

    # section C
    def members_in_state(self, country):
        members_amt = 0
        for member in self._members:
            if member.get_country() == country:
                members_amt += 1
        return members_amt

    # section D
    def add_member(self, m):
        if self.get_count() >= 20:
            return False

        if self.members_in_state(m.get_country()) >= 2:
            return False

        self._members.append(m)
        # Important: Update _count after adding, or rely solely on len(self._members)
        # I've updated get_count() to use len(self._members) for consistency.
        return True

# section E
def lead_committee(lst):
    max_committee = lst[0]
    for committee in lst:
        if committee.get_count() > max_committee.get_count():
            max_committee = committee

    return max_committee.get_sport_name()