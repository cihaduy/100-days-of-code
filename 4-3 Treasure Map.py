# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizonal = int(position[0]) 
vertical = int(position[1]) -1

if horizonal == 1:
  row1[vertical] = "X"
elif horizonal == 2:
  row2[vertical] = "X"
elif horizonal == 3:
  row3[vertical] = "X"
else:
  print("Out of range")

  



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")