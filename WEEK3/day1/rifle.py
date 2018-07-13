import unittest


def is_single_riffle(half1, half2, shuffled_deck):

    # Check if the shuffled deck is a single riffle of the halves
    l1 = len(half1)
    l2 = len(half2)
    l = len (shuffled_deck)
    i = 0
    j = 0
    for k in range (l):
        if(i<l1 and shuffled_deck[k] == half1[i]):
            i+=1
        elif(j<l2 and shuffled_deck[k] == half2[j]):
            j+=1
        else:
            return False
    return True


# Tests

class Test(unittest.TestCase):

    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


unittest.main(verbosity=2)
