#use unittest library to generate test cases

import  unittest
from fun_chap11 import get_formed_name, get_new_name

##class NamesTestCase(unittest.TestCase):
    ##'''Test fun_chap11.py'''
    ##def test_full_name(self):
        ##'''Can the function outputs correct full name?'''
        ##formatted_name = get_formed_name('lucas', 'park')
        ##self.assertEqual(formatted_name, 'Lucas Park')#here we test if the outcome equals 'Lucas Park'

##unittest.main()

class NewNameTest(unittest.TestCase):
    '''Test fun_chap11.py'''
    def test_full_name(self):
        formed_name = get_new_name('lucas', 'park')
        print(formed_name)
        self.assertEqual(formed_name, 'Lucas Park')

    def test_three_name(self):
        formed_name = get_new_name('lucas', 'park', 'j.')
        print(formed_name)
        self.assertEqual(formed_name, 'Lucas J. Park')

    def test_if_not_equal(self):
        self.assertNotEqual('a', 'b')
        print('a'!='b')

    def test_if_true(self):
        self.assertTrue(1<2)
        print(1<2)

    def test_if_not_true(self):
        self.assertFalse(1>=2)
        print(1>=2)

    def test_if_in(self):
        self.assertIn('a', 'about')
        print('a'in'about')

    def test_if_not_in(self):
        self.assertNotIn('b', 'help')
        print('b'in 'help')

if __name__ =='__main__':
    unittest.main()