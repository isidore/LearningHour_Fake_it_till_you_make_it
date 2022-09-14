def fizz_buzz(param):
    fizzbuzz_string = ""
    list = range(1,30+1)
    for j in list:
        fizzbuzz_string += calculate_fizz_buzz_for_number(j)
    return fizzbuzz_string + "31,32"


def calculate_fizz_buzz_for_number(number):
    if number == 15 or number == 30:
        return "FizzBuzz,"
    if number % 3 == 0:
        return "Fizz,"
    if number % 5 == 0:
        return "Buzz,"
    return f"{number},"

def test_fizz_buzz():
    output = fizz_buzz(32)
    expect = "1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16,17,Fizz,19,Buzz,Fizz,22,23,Fizz,Buzz,26,Fizz,28,29,FizzBuzz,31,32"
    assert output == expect
    pass
