# Data input
n = int(input("Please input number of rows \n"))
m = int(input("Please input number of columns \n"))
list_num = []
for i in range(n):
    row = [int(j) for j in input("Please input row %d \n" %(i+1)).split()]
    while len(row) != m:
        row = [int(j) for j in input("Please input correct row \n").split()]
    list_num.append(row)
print(list_num)

#Calculation workflow
counter = 0
summ = 0
for i in list_num:
    for j in i:
        if j >= 0:
            summ += j
            counter += 1
if summ == 0:
    print("No positive numbers found")
else:
    average_number = summ / counter
    print("Average number is ", average_number)