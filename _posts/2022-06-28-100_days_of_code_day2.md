---
title: 100 Days of Code
date:  2022-06-28 12:00:00 -500
categories: [code,python,100days]
tags: [python,code,learning,100days]
---

# 100 Days of Code

## Day 2

#### Exercise 1 - Data Types

Solution:
```python
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

print(first_digit + second_digit)
```


#### Exercise 2 - BMI Calculator
```python
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_as_float = float(height)
weight_as_float = float(weight)

bmi = weight_as_float / height_as_float ** 2
print(int(bmi))
```

#### Exercise 4 - Life in Weeks
```python
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
MAX_AGE = 90
DAYS_IN_YEAR = 365
WEEKS_IN_YEAR = 52
MONTHS_IN_YEAR = 12

current_age_as_int = int(age)
days_left = (MAX_AGE - current_age_as_int) * DAYS_IN_YEAR
weeks_left = (MAX_AGE - current_age_as_int) * WEEKS_IN_YEAR
months_left = (MAX_AGE - current_age_as_int) * MONTHS_IN_YEAR

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
```