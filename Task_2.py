# Data input
elements = [int(i) for i in input("Please input list elements \n").split()]

# Select the main number for comparison
main_number = int(input("Please define the number for comparison \n"))

# Defining the count of numbers
counter = 0

# Defining of the type of verification - bigger OR smaller numbers
decision = input(
    "Please choose what verification should be applied: Bigger numbers OR Smaller. Input 'B' or 'S' accordingly. \n").upper()
while decision != "B" and decision != "S":
    decision = input("Please input correct value: 'B' or 'S' \n").upper()

if decision == "B":
    for i in elements:
        if i > main_number and i != main_number:
            counter += 1
elif decision == "S":
    for i in elements:
        if i < main_number and i != main_number:
            counter += 1

# Results displaying
if counter == 0:
    if decision == "B":
        print("There is no numbers which are bigger than the ", main_number)
    else:
        print("There is no numbers which are smaller than the ", main_number)
else:
    if decision == "B":
        print("The number of bigger numbers than ", main_number, " is: ", counter)
    else:
        print("The number of smaller numbers than ", main_number, " is: ", counter)