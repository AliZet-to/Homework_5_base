#Data input
while True:
    string = input("Please input the string: \n")
    string = string.split(' ')
    counter = 0

#Calculation workflow
    for x in string:
        if string.count(x) == 1:
            counter += 1
    print(counter)
    another_search = input("Do you want make another search? Y / N \n").upper()
    if another_search == "N":
        break