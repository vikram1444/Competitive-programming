
import unittest


def reverse(list_of_chars):

    # Reverse the input list of chars in place
    l = len(list_of_chars)
    if(l == 0 or l == 1):
        return list_of_chars 
    limit = (l/2)
    for i in range (limit):
        (list_of_chars[i], list_of_chars[l-i-1] ) = (list_of_chars[l-i-1], list_of_chars[i])

    return list_of_chars

# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E','D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)
