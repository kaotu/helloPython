import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_input_3_should_return_fizz(self):
        number = 3
        result = fizz_buzz(number)
        self.assertEqual(result, 'fizz')

    def test_input_4_should_return_4(self):
        number = 4
        result = fizz_buzz(number)
        self.assertEqual(result, 4)

    def test_input_5_should_return_buzz(self):
        number = 5
        result = fizz_buzz(number)
        self.assertEqual(result, 'buzz')
        
    def test_input_8_should_return_8(self):
        number = 8
        result = fizz_buzz(number)
        self.assertEqual(result, 8)
        
    def test_input_15_should_return_FizzBuss(self):
        number = 15
        result = fizz_buzz(number)
        self.assertEqual(result, 'FizzBuzz')
        
    def test_input_16_should_return_16(self):
        number = 16
        result = fizz_buzz(number)
        self.assertEqual(result, number)

def fizz_buzz(number):
    if number % 3  == 0 and number % 5 == 0:
        result = 'FizzBuzz'
    elif number % 5 == 0:
        result = 'buzz'
    elif number % 3 == 0:
        result = 'fizz'
    else:
        result = number
    
    return result

unittest.main()
        
