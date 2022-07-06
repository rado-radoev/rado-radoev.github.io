from re import L
from unicodedata import name

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

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

if score < 10 and score > 90:
  print(MESSAGE_1)
elif score >= 40 and score <= 50:
  print(MESSAGE_2)
else:
  print(MESSAGE_3)
