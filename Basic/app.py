#Comments

# single line comment

'''
multi
line
comment
'''

# Python is an interpreted language

# Python is a dynamically typed language
import random
from random import Random

name = "kanishk"
age = 24
salary = 150000.00
handsome = True

# Types of data in python
# numbers
# strings
# characters
# None
# booleans

# print function
print("Hi I am python, daro mujhse hissss!!!")
print(name)
print(age)
print(salary)
print(handsome)

# formatted print
print("My name is " + name + " and I am " + str(age) + " years old making " + str(salary) + " Rupees.")
print(f"My name is {name} and I am {age} years old making {salary} Rupees.")

# Operators
# Mathematical operators
a = 5
b = 2
#     addition
sum = a + b
print(sum)
#     subtraction
difference = a - b
print(difference)
#     multiplication
product = a * b
print(product)
#     fractional division
fraction = a / b
print(fraction)
#     integral division
integral = a // b
print(integral)
#     remainder or modulus
remainder = a % b
print(remainder)
#     power or exponent
exponent = a ** b
print(exponent)

# String operators
# concatination and other functions of string modules

# logical operators
# AND && and
# OR || or
# NOT ! not

# relational operators
# increment +=
number = 3
number += 7
print(number)

# decrement -=
number -= 10
print(number)

# Conditional
age = 78
if age >= 60:
    print("you are senior citizen")
elif 60 > age >= 18:
    print("you are adult")
else:
    print("you are a kid. go home!")

# Loop
# while
count = 10
while count > 0:
    print(f"count is {count}")
    count -= 1

# for
for i in range(2, 21, 2):
    print(i)

# array, linkedlist, stack, queue
# List - mutable in nature - can be modified
names = ["kanishk", "karan", "vinay", "kunal"]

for name in names:
    print(name)

names.append("pooja")
print(names)
names.insert(2, "keshav")
print(names[:-10])
names.remove("vinay")
print(names)
names.pop()
print(names)

# numbers = [i for i in range(5, 51, 5)]
numbers = [0 for i in range(5)]

print(numbers)

# tuple
# immutable list
members = ("kanishk", "karan")

print(members)

# ceo = members[0]
# cto = members[1]
ceo, cto = members
print(f"ceo is {ceo} and cto is {cto}")


# Dictionary
number_in_word = {
    1 : "one",
    2 : "two",
    3 : "three"
}

input_number = [2, 3, 1, 2, 3, 2, 1, 2, 2]
for number in input_number:
    print(number_in_word[number], end=" ")