# This program calculates how many tiles you will need
# when tiling a wall or floor (in m2)

lenght = float(input("enter room lenght: "))
width = float(input("enter room width: "))

#lenght = 3.5
#width = 2.3

area = lenght * width

needed = area * 1.05

print("You need", needed, "tiles in metres squared")