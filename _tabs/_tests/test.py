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
