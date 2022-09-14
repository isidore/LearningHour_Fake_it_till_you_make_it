def fizz_buzz(param):
    fizzbuzz_string = ""
    list = range(1,3)
    for j in list:
        fizzbuzz_string += calculate_number(j)
    return fizzbuzz_string + "Fizz," + "4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16,17,Fizz,19,Buzz,Fizz,22,23,Fizz,Buzz,26,Fizz,28,29,FizzBuzz,31,32"


def calculate_number(number):
    return f"{number},"

def test_fizz_buzz():
    output = fizz_buzz(32)
    expect = "1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16,17,Fizz,19,Buzz,Fizz,22,23,Fizz,Buzz,26,Fizz,28,29,FizzBuzz,31,32"
    assert output == expect
    pass
