import unittest

import script as main


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        print('about  to test a function')

    def test_do_stuff(self):
        '''
        Testing the normal functionality
        '''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        '''
        testing string input
        '''
        test_param = 'baba'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        '''
        testing empty list 
        '''
        test_param = []
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'wrong')

    def test_do_stuff4(self):
        '''
        testing None input 
        '''
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'wrong')

    def test_do_stuff5(self):
        '''
        testing empty string
        '''
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'wrong')

    def tearDown(self) -> None:
        print('cleaning up')


if __name__ == '__main__':
    unittest.main()

# The idea behind error testing is trying to break the function and then fix the error
# Also keep in mind to make the tests as easy to read as possible
# run python -m unittest to run all the tests in unison (even if there in different files)
# remember to add if __name__ == '__main__' to all the test files
# add -v to get more info on the tests
