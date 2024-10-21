#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
            number *= -1
            last_digit = number % 10
            print("{:d}".format(last_digit))        
    elif number == 0:
         print("{:d}".format(number))
    else:
       last_digit = number % 10
       print("{:d}".format(last_digit))    ()
