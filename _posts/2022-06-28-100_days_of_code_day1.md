---
title: 100 Days of Code
date:  2022-06-28 12:00:00 -500
categories: [code,python,100days]
tags: [python,code,learning,100days]
---

# 100 Days of Code
## Day 1

#### Exercise 1 - Printing

Solution:
```python
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
```

#### Exercise 3 - Input Function

Solution:
```python
print(len(input("What is your name?")))
```

#### Exercise 4 - Variables

Solution:
```python
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c = a
a = b
b = c

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
```

#### Band name generator

Solution:
```python
#1. Create a greeting for your program.
print ("Hello there maty!")
#2. Ask the user for the city that they grew up in.
city = input("What city did you grow up in?\n")
#3. Ask the user for the name of a pet.
pet_name = input("What is the name of your pet?\n")
#4. Combine the name of their city and pet and show them their band name.
band_name = city + " " + pet_name + "\n"
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end
print("Your band name, could be: " + band_name)
```
