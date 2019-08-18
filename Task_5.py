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

#Ascending Sorting
for i in list_num:
    i.sort()
    print(i)