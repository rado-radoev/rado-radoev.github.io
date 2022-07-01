---
title: 100 Days of Code
date:  2022-06-30 12:00:00 -500
categories: [code,python,100days]
tags: [python,code,learning,100days]
---

# 100 Days of Code

## Day 3

#### Exerice 1 - Odd or Even
> modulus % 
> 
> even number % 2 = 0
> 
> odd number % 2 = 1
>
```python
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number_as_int = int(number)

if (number_as_int % 2 == 0):
    print("This is an even number.")
else:
    print("This is an odd number.")
```

#### Exercise 2 - BMI 2.0

> if condition:
> > elif condition:
> 
> else
```python
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height ** 2
rounded_bmi = round(bmi)

if (bmi < 18.5):
    print (f"Your BMI is {rounded_bmi}, you are underweight.") 
elif (bmi > 18.5 and bmi < 25):
    print (f"Your BMI is {rounded_bmi}, you have a normal weight.") 
elif (bmi > 25 and bmi < 30):
    print (f"Your BMI is {rounded_bmi}, you are slightly overweight.") 
elif (bmi > 30 and bmi < 35):
    print (f"Your BMI is {rounded_bmi}, you are obese")
else:
    print (f"Your BMI is {rounded_bmi}, you are clinically obese.")
```


#### Exerice 3 - Leap year calculator

```python
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
leap = False

if year % 100 == 0:
    leap = False
elif year % 4 == 0: 
    leap = True
elif year % 400 == 0:
    leap = True


print("Leap year.") if leap else print("Not leap year.")
```