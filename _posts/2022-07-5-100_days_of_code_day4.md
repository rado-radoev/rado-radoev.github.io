---
title: 100 Days of Code
date:  2022-06-30 12:00:00 -500
categories: [code,python,100days]
tags: [python,code,learning,100days]
---

# 100 Days of Code

## Day 4

#### Exerice 4 - True love calculator
```python
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
true_dict = {
  "T": 0,
  "R": 0,
  "U": 0,
  "E": 0
}

love_dict = {
  "L": 0,
  "O": 0,
  "V": 0,
  "E": 0
}

name1_arr = list(name1.upper())
name2_arr = list(name2.upper())

for letter in name1_arr:
  if letter in true_dict.keys():
    true_dict[letter] += 1

  if letter in love_dict.keys():
    love_dict[letter] +=1

for letter in name2_arr:
  if letter in true_dict.keys():
    true_dict[letter] += 1

  if letter in love_dict.keys():
    love_dict[letter] +=1

total_true_matches = sum(true_dict.values())
total_love_matches = sum(love_dict.values())

score = int(f"{total_true_matches}{total_love_matches}")

MESSAGE_1 = f"Your score is {score}, you go together like coke and mentos."
MESSAGE_2 = f"Your score is {score}, you are alright together."
MESSAGE_3 = f"Your score is {score}."

if score < 10 or score > 90:
  print(MESSAGE_1)
elif score >= 40 and score <= 50:
  print(MESSAGE_2)
else:
  print(MESSAGE_3)
```

#### Challenge Day 4 - Game Book
```python
import sys


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()
if direction != "left":
  print("Fall into a hole. Game over.")
  sys.exit()

lake = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
if lake != "wait":
  print("Attacked by trout. Game Over.")
  sys.exit()

door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
if door == "red":
  print('Burned by fire.Game Over.')
  sys.exit()
elif door == "blue":
  print("Eaten by beasts. Game Over.")
  sys.exit()
elif door == "yellow":
  print("You win.")
else:
  print("Game Over.")

sys.exit()
```


#### Exercies 1 - Heads or Tails
```python

```
