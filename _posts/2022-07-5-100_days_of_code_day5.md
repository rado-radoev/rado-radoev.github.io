---
title: 100 Days of Code
date:  2022-07-13 12:00:00 -500
categories: [code,python,100days]
tags: [python,code,learning,100days]
---

# 100 Days of Code

## Day 5

#### Exerice 1 - Average Height ####
```python
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
total_students = 0
total_heights = 0

for height in student_heights:
  total_students += 1
  total_heights += height

average_height = total_heights / total_students

# print(total_students)
# print(total_heights)
# print("{:.0f}".format(average_height))
print(round(average_height))

#Write your code below this row 👇
```

#### Exercise 2 - Highest Score ####
```python
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max_score = 0

for score in student_scores:
  if score > max_score:
    max_score = score

print(f"The highest score in the class is: {max_score}")
```
#### Exercise 3 - Adding Even Numbers ####
```python
#Write your code below this row 👇
total = 0
for number in range(2, 101, 2):
  total += number

print(total)
```

#### Exercise 4 - FizzBuzz ####
```python
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
```

#### Boss - Password Generator ####
```python

```
