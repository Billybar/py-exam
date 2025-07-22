# Assuming all classes are in the same file
class Employee:
    def __init__(self, name):
        self._name = name

    def get_points(self):
        return 4

    def get_name(self):
        return self._name

class RegularEmployee(Employee):
    def __init__(self, name, years):
        super().__init__(name)
        self._years = years

    def get_points(self):
        # Gets points from Employee and adds 1 point for each year of experience
        return super().get_points() + self._years

class UnionMember(Employee):
    def __init__(self, name, years, union_years=0):
        super().__init__(name)
        self._union_years = union_years
        self._years = years  # Based on the table, RegularEmployee also has 'years',
        # UnionMember constructor takes 'years' and 'union_years'. The problem statement
        # for union_member states 'union_years' only. Assuming 'years' for UnionMember
        # is also relevant as an employee type.

    def get_points(self):
        # Gets points twice of an employee and adds 2 points for each year as a union member
        return (super().get_points() * 2) + (self._union_years * 2)


class Technician(Employee):
    def __init__(self, name, products):
        super().__init__(name)
        self._products = products

    def get_points(self):
        # Gets points from Employee and adds 1 point for each product
        return super().get_points() + self._products


class TeamLeader(Employee):
    def __init__(self, name, years,
                 employees=None):   # 'years' parameter for TeamLeader is assumed based on the
                                    # constructor description, although not explicitly used for points.
                                    # The prompt states "no workers in the team" which means no employees
                                    # initially, so `employees` should default to an empty list.
        super().__init__(name)
        self._years = years  # Assumed from constructor description.
        if employees is None:
            self._employees = []
        else:
            self._employees = employees

    def get_points(self):
        # Gets points from Employee and adds total points of all employees in the team
        team_points = 0
        for employee in self._employees:
            team_points += employee.get_points()
        return super().get_points() + team_points

    def add_employee(self, employee):
        self._employees.append(employee)


def is_accepted(lst):
    """
    Checks if the proposal is accepted based on employee votes.
    Regular employees and technicians support the proposal.
    Union members and team leaders oppose the proposal.
    The proposal is accepted if the total points for it are greater than the total
    points against it.
    """
    for_points = 0
    against_points = 0

    for employee in lst:
        if isinstance(employee, RegularEmployee) or isinstance(employee, Technician):
            for_points += employee.get_points()
        elif isinstance(employee, UnionMember) or isinstance(employee, TeamLeader):
            against_points += employee.get_points()

    return for_points > against_points


import unittest


# Assuming the classes and is_accepted function are defined as in the previous response
# (copy-paste the class definitions and is_accepted function here if running this file separately)

class TestEmployeeClasses(unittest.TestCase):

    def test_employee_get_points(self):
        emp = Employee("Alice")
        self.assertEqual(emp.get_points(), 4)

    def test_regular_employee_get_points(self):
        reg_emp_0_years = RegularEmployee("Bob", 0)
        self.assertEqual(reg_emp_0_years.get_points(), 4)  # 4 (base) + 0 (years)

        reg_emp_5_years = RegularEmployee("Charlie", 5)
        self.assertEqual(reg_emp_5_years.get_points(), 9)  # 4 (base) + 5 (years)

    def test_union_member_constructor_and_get_points(self):
        # Test with default union_years
        union_mem_default = UnionMember("David", 3)
        self.assertEqual(union_mem_default.get_points(), 8)  # (4 * 2) + (0 * 2)

        # Test with specified union_years
        union_mem_2_years = UnionMember("Eve", 5, 2)
        self.assertEqual(union_mem_2_years.get_points(), 12)  # (4 * 2) + (2 * 2)

        union_mem_0_years_union = UnionMember("Frank", 1, 0)
        self.assertEqual(union_mem_0_years_union.get_points(), 8)  # (4 * 2) + (0 * 2)

    def test_technician_get_points(self):
        tech_0_products = Technician("Grace", 0)
        self.assertEqual(tech_0_products.get_points(), 4)  # 4 (base) + 0 (products)

        tech_10_products = Technician("Heidi", 10)
        self.assertEqual(tech_10_products.get_points(), 14)  # 4 (base) + 10 (products)

    def test_team_leader_constructor_and_get_points(self):
        # Test empty team
        team_leader_empty = TeamLeader("Ivan", 2)
        self.assertEqual(team_leader_empty.get_points(), 4)  # 4 (base) + 0 (team points)

        # Test with a team of various employees
        emp1 = RegularEmployee("Alice", 1)  # 4 + 1 = 5 points
        emp2 = Technician("Bob", 3)  # 4 + 3 = 7 points
        emp3 = UnionMember("Charlie", 0, 1)  # (4 * 2) + (1 * 2) = 10 points

        team_leader_with_team = TeamLeader("David", 5)
        team_leader_with_team.add_employee(emp1)
        team_leader_with_team.add_employee(emp2)
        team_leader_with_team.add_employee(emp3)

        # Expected team points: 5 + 7 + 10 = 22
        # Team leader total points: 4 (base) + 22 (team points) = 26
        self.assertEqual(team_leader_with_team.get_points(), 26)

        # Test with a team leader managing another team leader
        sub_team_leader = TeamLeader("SubLeader", 1)
        sub_team_leader.add_employee(RegularEmployee("Zoe", 2))  # 4 + 2 = 6 points

        main_team_leader = TeamLeader("MainLeader", 10)
        main_team_leader.add_employee(sub_team_leader)
        main_team_leader.add_employee(Technician("Yara", 5))  # 4 + 5 = 9 points

        # Sub-team leader points: 4 (base) + 6 (Zoe) = 10
        # Main team leader total points: 4 (base) + 10 (SubLeader) + 9 (Yara) = 23
        self.assertEqual(main_team_leader.get_points(), 23)


class TestIsAcceptedFunction(unittest.TestCase):

    def test_all_for(self):
        employees = [
            RegularEmployee("Alice", 5),  # 9 points (for)
            Technician("Bob", 10)  # 14 points (for)
        ]
        self.assertTrue(is_accepted(employees))  # 23 > 0

    def test_all_against(self):
        employees = [
            UnionMember("Charlie", 1, 2),  # 12 points (against)
            TeamLeader("David", 0)  # 4 points (against)
        ]
        self.assertFalse(is_accepted(employees))  # 0 < 16

    def test_mixed_accepted(self):
        employees = [
            RegularEmployee("Alice", 5),  # 9 points (for)
            Technician("Bob", 10),  # 14 points (for)
            UnionMember("Charlie", 1, 2),  # 12 points (against)
            TeamLeader("David", 0)  # 4 points (against)
        ]
        # For: 9 + 14 = 23
        # Against: 12 + 4 = 16
        self.assertTrue(is_accepted(employees))  # 23 > 16

    def test_mixed_not_accepted(self):
        employees = [
            RegularEmployee("Alice", 0),  # 4 points (for)
            UnionMember("Charlie", 0, 5),  # (4 * 2) + (5 * 2) = 18 points (against)
        ]
        # For: 4
        # Against: 18
        self.assertFalse(is_accepted(employees))  # 4 < 18

    def test_tie(self):
        employees = [
            RegularEmployee("Alice", 4),  # 8 points (for)
            UnionMember("Charlie", 0, 2),  # (4 * 2) + (2 * 2) = 12 points (against)
            Technician("Bob", 4)  # 8 points (for)
        ]
        # For: 8 + 8 = 16
        # Against: 12
        self.assertTrue(is_accepted(employees))  # 16 > 12

        employees_tie_against_wins = [
            RegularEmployee("Alice", 0),  # 4 points (for)
            Technician("Bob", 0),  # 4 points (for)
            UnionMember("Charlie", 0, 2),  # 12 points (against)
        ]
        # For: 4 + 4 = 8
        # Against: 12
        self.assertFalse(is_accepted(employees_tie_against_wins))  # 8 < 12

    def test_empty_list(self):
        employees = []
        self.assertFalse(is_accepted(employees))  # 0 > 0 is False

    def test_team_leader_with_complex_team(self):
        # A more complex scenario involving nested TeamLeaders
        reg_emp = RegularEmployee("Alice", 2)  # 6 points
        tech = Technician("Bob", 3)  # 7 points
        union_mem = UnionMember("Charlie", 0, 1)  # 10 points

        sub_team_leader1 = TeamLeader("SubLeader1", 0)
        sub_team_leader1.add_employee(reg_emp)
        sub_team_leader1.add_employee(tech)
        # SubLeader1 points: 4 (base) + 6 + 7 = 17 points

        sub_team_leader2 = TeamLeader("SubLeader2", 0)
        sub_team_leader2.add_employee(union_mem)
        # SubLeader2 points: 4 (base) + 10 = 14 points

        main_team_leader_for = TeamLeader("MainLeaderFor", 0)
        main_team_leader_for.add_employee(RegularEmployee("Emma", 1))  # 5 points
        # MainLeaderFor points: 4 + 5 = 9 points (against, but team member adds points for)

        main_team_leader_against = TeamLeader("MainLeaderAgainst", 0)
        main_team_leader_against.add_employee(sub_team_leader1)
        main_team_leader_against.add_employee(sub_team_leader2)
        # MainLeaderAgainst points: 4 (base) + 17 (sub1) + 14 (sub2) = 35 points (against)

        employees = [
            main_team_leader_for,  # 9 points (against)
            main_team_leader_against,  # 35 points (against)
            RegularEmployee("Fiona", 10),  # 14 points (for)
            Technician("George", 20)  # 24 points (for)
        ]
        # For: 14 + 24 = 38
        # Against: 9 + 35 = 44
        self.assertFalse(is_accepted(employees))  # 38 < 44

        employees_accepted_complex = [
            RegularEmployee("A", 10),  # 14 (for)
            Technician("B", 10),  # 14 (for)
            UnionMember("C", 0, 1),  # 10 (against)
            TeamLeader("D", 0, [RegularEmployee("E", 0)])  # Team Leader: 4 + (4+0) = 8 (against)
        ]
        # For: 14 + 14 = 28
        # Against: 10 + 8 = 18
        self.assertTrue(is_accepted(employees_accepted_complex))  # 28 > 18


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)