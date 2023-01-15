import sys

xandy = sys.stdin.readline().strip().split(",")
X = int(xandy[0])
Y = int(xandy[1])
array = []

for i in range(0,X):
    array.append([])
for number, row in enumerate(array):
    for i in range(0,Y):
        row.append(number*i)
        i += 1 

print(array)
