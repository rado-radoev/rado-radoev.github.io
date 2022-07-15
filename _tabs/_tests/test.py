import string
import random

alphabet = list(string.ascii_letters)
digits = list(string.digits)
symbols = list(string.punctuation)

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(alphabet))

for char in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
  password_list.append(random.choice(digits))

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")

# === BUNCH A NONSESE BELOW ===
# map = [alphabet, digits, symbols]

# random_list = random.randint(0, len(map) - 1)
# random_char = random.randint(0, len(map[random_list]) - 1 )
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input("How many symbols would you like in your password?\n"))
# nr_numbers = int(input("How many numbers would you like in your password?\n"))

# # print(map[random_list][random_char])
# pw_letters = []
# pw_digits = []
# pw_symbols = []

# for letter in range(1, nr_letters + 1):
#   random_char = random.randint(0, len(alphabet) - 1 )
#   pw_letters.append(alphabet[random_char])

# for digit in range(1, nr_numbers + 1):
#   random_char = random.randint(0, len(digits) - 1 )
#   pw_digits.append(digits[random_char])

# for symbol in range(1, nr_symbols + 1):
#   random_char = random.randint(0, len(symbols) - 1 )
#   pw_symbols.append(symbols[random_char])

# ordered_pass = [pw_letters, pw_digits, pw_symbols]
# flattened_pass = [element for sublist in ordered_pass for element in sublist]
# print(''.join(flattened_pass))

# unordered_pass = {''.join(flattened_pass)}
# # unordered_pass.update(ordered_pass)
# print(''.join(unordered_pass))
# # for x in ordered_pass:
# #   for y in x:
# #     unordered_pass.update(y)


