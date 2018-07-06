import unittest


def get_permutations(string):

    # Generate all permutations of the input string
    solution = []
    l = len(string)
    if(l==0 or l==1):
        return set([string])
    for i in range (l):
        newstring = string[0:i]+string[i+1:l]
        newlist = get_permutations(newstring)
        for k in newlist:
            solution.append(string[i]+k)
    return set(solution)



# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
