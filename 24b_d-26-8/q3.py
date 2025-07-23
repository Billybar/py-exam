import unittest

# Question 3, Section A: min_str
def min_str(lst: list[str]) -> str:
    # Base case: If the list contains only one string, that string is the minimum.
    if len(lst) == 1:
        return lst[0]
    else:
        # Recursive step:
        # Get the first string in the current sublist.
        first_str = lst[0]
        # Recursively find the minimum string in the rest of the list.
        min_in_rest = min_str(lst[1:])

        # Compare the length of the first string with the minimum found in the rest.
        if len(first_str) <= len(min_in_rest):
            return first_str
        else:
            return min_in_rest

# Question 3, Section B: search
def search(s1: str, s2: str) -> bool:
    # Base Case 1: If s2 is an empty string, it is considered to be found in any s1.
    if not s2:
        return True

    # Base Case 2: If s1 is shorter than s2, s2 cannot be a substring of s1.
    if len(s1) < len(s2):
        return False

    # Check if the current prefix of s1 matches s2.
    # This replaces the explicit for loop with a direct string slice comparison.
    # This operation is handled efficiently by Python's built-in string methods.
    if s1[:len(s2)] == s2:
        return True
    else:
        # Recursive step: If no match at the current position,
        # try searching in the rest of s1 (s1 without its first character).
        return search(s1[1:], s2)


class TestQ3Functions(unittest.TestCase):

    def test_min_str(self):
        # Test Case 1: Basic list
        self.assertEqual(min_str(["apple", "banana", "cat"]), "cat", "Test Case 1 Failed: min_str(['apple', 'banana', 'cat'])")

        # Test Case 2: List with strings of same minimum length, should return the first one encountered
        self.assertEqual(min_str(["dog", "cat", "elephant"]), "dog", "Test Case 2 Failed: min_str(['dog', 'cat', 'elephant'])")

        # Test Case 3: Single element list
        self.assertEqual(min_str(["hello"]), "hello", "Test Case 3 Failed: min_str(['hello'])")

        # Test Case 4: Empty strings
        self.assertEqual(min_str(["", "a", "bb"]), "", "Test Case 4 Failed: min_str(['', 'a', 'bb'])")

        # Test Case 5: Mixed lengths
        self.assertEqual(min_str(["longest", "short", "medium", "a"]), "a", "Test Case 5 Failed: min_str(['longest', 'short', 'medium', 'a'])")

        # Test Case 6: Numbers as strings
        self.assertEqual(min_str(["123", "12", "1"]), "1", "Test Case 6 Failed: min_str(['123', '12', '1'])")

    def test_search(self):
        # Test Case 1: s2 exists in s1
        self.assertTrue(search("ewxabcs", "abc"), "Test Case 1 Failed: search('ewxabcs', 'abc')")

        # Test Case 2: s2 does not exist in s1 (example from problem)
        self.assertFalse(search("a", "abc"), "Test Case 2 Failed: search('a', 'abc')")

        # Test Case 3: s2 is at the beginning of s1
        self.assertTrue(search("abcdef", "abc"), "Test Case 3 Failed: search('abcdef', 'abc')")

        # Test Case 4: s2 is at the end of s1
        self.assertTrue(search("abcdef", "def"), "Test Case 4 Failed: search('abcdef', 'def')")

        # Test Case 5: s2 is in the middle of s1
        self.assertTrue(search("xyzabc123", "abc"), "Test Case 5 Failed: search('xyzabc123', 'abc')")

        # Test Case 6: s2 is longer than s1
        self.assertFalse(search("short", "longer"), "Test Case 6 Failed: search('short', 'longer')")

        # Test Case 7: s2 is an empty string (should always return True)
        self.assertTrue(search("any_string", ""), "Test Case 7 Failed: search('any_string', '')")
        self.assertTrue(search("", ""), "Test Case 8 Failed: search('', '')")

        # Test Case 9: s1 is empty, s2 is not empty
        self.assertFalse(search("", "a"), "Test Case 9 Failed: search('', 'a')")

        # Test Case 10: s2 is s1 itself
        self.assertTrue(search("test", "test"), "Test Case 10 Failed: search('test', 'test')")

        # Test Case 11: No match, but partial matches exist
        self.assertFalse(search("banana", "banaX"), "Test Case 11 Failed: search('banana', 'banaX')")

        # Test Case 12: s2 with special characters
        self.assertTrue(search("hello-world!", "-world"), "Test Case 12 Failed: search('hello-world!', '-world')")

        # Test Case 13: s2 not found, and s1 is long
        self.assertFalse(search("thisisalongstringwithoutthesubstring", "xyz"), "Test Case 13 Failed: search('thisisalongstringwithoutthesubstring', 'xyz')")

# To run the tests, uncomment the following lines:
# if __name__ == '__main__':
#     unittest.main(argv=['first-arg-is-ignored'], exit=False)
