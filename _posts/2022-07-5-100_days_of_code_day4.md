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
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.

#Write the rest of your code below this line 👇
coin_toss = random.randint(0, 2)

if coin_toss:
  print("Heads")
else:
  print("Tails")
```

#### Exercise 2 - Banker Roulette
```python
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number_of_people = len(names)
random_person = random.randint(0, number_of_people - 1)

print(f"{names[random_person]} is going to buy the meal today!")

```

#### Exercise 4 - Treasure map ####
```python
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
TREASURE_MARK = "X"

rowCol = list(position)
col = int(rowCol[0])
row = int(rowCol[1])

row -= 1
col -= 1

if row < 0:
  row = 0
elif row >= 3:
  row = -1

if col < 0:
  col = 0
elif col >= 3:
  col = -1

map[row][col] = TREASURE_MARK

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
```
