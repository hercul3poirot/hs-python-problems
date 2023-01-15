import sys 

general = [x for x in range(1000,3001)]
for number in general:
    i = 0
    for digit in str(number):
        if int(digit) % 2 == 0:
            i += 1
    if i != len(str(number)):
        general.remove(number)    
print(general)
