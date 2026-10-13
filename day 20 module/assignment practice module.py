import math


# Square root of number

n = int(input("enter the no. : "))
sqr_t = math.sqrt(n)
print(f"The square root of the no is : {sqr_t}")


# area of the circle

r = int(input("enter the radius : "))
area = math.pi * math.pow(r,2)
print(f"The area of a circle with radius {r} is {area:.2f}")



# random no generation

from random import randint

die = randint(1,6)
print(f"You rolled a : {die}")


# importing from a custum module calculator
import calculator

resultAdd = calculator.add(10,5)
resultmul = calculator.multiply(2,3)

print(f"Addition : {resultAdd}")
print(f"multiplication : {resultmul}")


# alliasing a module

import datetime as dt

today = dt.date.today()
print(f"Today's date is : {today}")

import temperature as t

print(f"25 degree celcius to farheniet : {t.celsius_to_fahrenheit(25):.1f}")
print(f"98F farheniet to celsius : {t.fahrenheit_to_celcius(98):.1f}")
