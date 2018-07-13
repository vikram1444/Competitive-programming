import unittest


def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    res = []
    l1 = len(my_list)
    l2 = len(alices_list)
    i = 0
    j = 0
    while(i<l1 and j<l2):
        if(my_list[i]<alices_list[j]):
            res.append(my_list[i])
            i+=1
        else:
            res.append(alices_list[j])
            j+=1
            
    while(i<l1):
        res.append(my_list[i])
        i+=1
    
    while(j<l2):
        res.append(alices_list[j])
        j+=1
    return res


# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
