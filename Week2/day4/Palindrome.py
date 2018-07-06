
import unittest


def has_palindrome_permutation(the_string):
    # Check if any permutation of the input is a palindrome
    l = len(the_string)
    dictn = {}
    for i in range (l):
        n = dictn.setdefault(the_string[i], 0)
        dictn[the_string[i]]=n+1
        
    if (l%2==0):
        for x in dictn.keys():
            if (dictn[x]%2!=0):
                return False
    else:
        flag = False
        for x in dictn.keys():
            if (dictn[x]%2!=0):
                if(flag == True):
                    return False
                else:
                    flag = True
    return True




# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
