import unittest


def find_repeat(arr):

    # Find a number that appears more than once
    up = len(arr)-1
    lo = 1
    while(lo<up):
         mid = (lo+up)/2
         llo = lo
         lup = mid
         ulo = mid+1
         uup = up
         ldist = lup - llo + 1
         count = 0
         for x in arr:
             if(x>=llo and x<=lup):
                 count+=1
         if (count>ldist):
             lo = llo
             up = lup
         else:
             lo = ulo
             up = uup
    return lo



# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
