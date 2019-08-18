# Data input
n = int(input("Please input number of rows \n"))
m = int(input("Please input number of columns \n"))
list_num = []
for i in range(n):
    row = [int(j) for j in input("Please input row %d \n" % (i + 1)).split()]
    while len(row) != m:
        row = [int(j) for j in input("Please input correct row \n").split()]
    list_num.append(row)
print(list_num)

#Calculation workflow
minimum = list_num[0][0]
min_num = 0
for i in range(len(list_num)):
    if min(list_num[i]) < minimum:
        minimum = min(list_num[i])
        min_num = i
print(minimum)
print(list_num[min_num])