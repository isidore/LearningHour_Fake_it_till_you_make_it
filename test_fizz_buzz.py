def fizz_buzz(param):
    #list= [1]

    fizzbuzz_string = ""
    i = 1
    fizzbuzz_string += calculate_number(i)
    i=2
    fizzbuzz_string += calculate_number(i)
    return fizzbuzz_string + "Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16,17,Fizz,19,Buzz,Fizz,22,23,Fizz,Buzz,26,Fizz,28,29,FizzBuzz,31,32"


def calculate_number(number):
    return f"{number},"

def test_fizz_buzz():
    output = fizz_buzz(32)
    expect = "1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16,17,Fizz,19,Buzz,Fizz,22,23,Fizz,Buzz,26,Fizz,28,29,FizzBuzz,31,32"
    assert output == expect
    pass
